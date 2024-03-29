import datetime
import logging
from abc import abstractmethod

from mediaforeman.media_collection import MediaCollection
from mediaforeman.media_file import MediaFile
from mediaforeman.analyses.analysis_result import AnalysisResult
from mediaforeman.util.media_file_type_detector import MediaFileTypeDetector
from mediaforeman.analyses.analysis_issue_error_encountered import AnalysisIssueErrorEncountered
from mediaforeman.analyses.analysis_issue_media_skipped import AnalysisIssueMediaSkipped

_log = logging.getLogger()

class AnalysisBase(object):

    def __init__(self):
        self.ElapsedTime = None
        
    @abstractmethod
    def RunAnalysisOnCollection(self, mediaColl):
        pass
    
    @abstractmethod
    def RunAnalysisOnFile(self, mediaFile):
        pass
    
    @abstractmethod
    def GetAnalysisType(self):
        pass
    
    @abstractmethod 
    def IsCollectionAnalysis(self):
        pass
    
    @abstractmethod
    def IsFileAnalysis(self):
        pass
    
    @abstractmethod
    def FixIssues(self, media):
        pass
    
    @abstractmethod
    def CanFix(self):
        return True
    
    @abstractmethod
    def ShouldRun(self, media):
        if(isinstance(media, MediaFile)):
            if(self.RequiresMediaFileType() == True):
                detector = MediaFileTypeDetector()
                if(detector.IsExtensionOnPathAMatch(media.BasePath) == False):
                    return False
            
        return True    

    def LogAnalysisResult(self, analysisResult):
        if(analysisResult.HasIssues == False):
            msg = "{}: no issues found for file {}".format(
                self.GetAnalysisType(), analysisResult.Media.BasePath
            )
        else:
            issues = '\n\t- '.join([issue.GetText() for issue in analysisResult.IssuesFound])
            msg = "{}: analysis issue list against file {}\n\t- {}\n".format(
                self.GetAnalysisType(), analysisResult.Media.BasePath, issues
            )
            
        _log.info(msg)
    
    def RunAnalysis(self, media):
        startTime = datetime.datetime.now()
        _log.info("running analysis '{}' against type {} with path {}".format(
            self.GetAnalysisType(), type(media), media.BasePath
        ))

        result = AnalysisResult()
        result.AnalysisType = self.GetAnalysisType()
        result.Media = media
        
        '''include a reference to what ran the analysis'''
        result.AnalysisObj = self

        try:
            if(self.ShouldRun(media) == False):
                result.WasProcessed = False
                _log.warn("skipping file analysis on media {}, it is not eligible".format(media.BasePath))
                
            elif(isinstance(media, MediaCollection)):
                if(self.IsFileAnalysis() == True):
                    for mediaFile in media.MediaFiles:
                        if(self.ShouldRun(mediaFile) == False):
                            result.IssuesFound.append(AnalysisIssueMediaSkipped(
                                mediaFile, "not eligible for analysis type {}".format(self.GetAnalysisType())
                            ))
                        else:
                            result.IssuesFound.extend(self.RunAnalysisOnFile(mediaFile)) 
                else:
                    result.IssuesFound = self.RunAnalysisOnCollection(media)
            
            elif(isinstance(media, MediaFile)):
                result.IssuesFound = self.RunAnalysisOnFile(media)
                
        except Exception as err:
            errMsg = "failed to run analysis on media at path {}: {}".format(media.BasePath, err)
            _log.error(errMsg)
            result.IssuesFound = [AnalysisIssueErrorEncountered(media, errMsg)]
            
        result.ElapsedInMicroSecs = (datetime.datetime.now() - startTime).microseconds
        result.HasIssues = (len(result.IssuesFound) > 0)
        
        self.LogAnalysisResult(result)
        
        return result
