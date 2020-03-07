'''
Created on Dec 30, 2019

@author: kieranemiller
'''
import datetime
import logging
from abc import abstractmethod

from kem.mediaforeman.media_collection import MediaCollection
from kem.mediaforeman.media_file import MediaFile
from kem.mediaforeman.analyses.analysis_result import AnalysisResult

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
    def ShouldRun(self, media):
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
            if(isinstance(media, MediaCollection)):
                result.IssuesFound = self.RunAnalysisOnCollection(media)
            
            elif(isinstance(media, MediaFile)):
                if(self.ShouldRun(media)):
                    result.IssuesFound = self.RunAnalysisOnFile(media)
                else:
                    _log.warn("skipping file analysis on media {}, it is not eligible".format(media.BasePath))
            
            else:
                raise ValueError("unknown run analysis media parameter")
            
        except Exception as err:
            errMsg = "failed to run analysis on media at path {}: {}".format(media.BasePath, err)
            _log.error(errMsg)
            #raise err
            
        result.ElapsedInMicroSecs = (datetime.datetime.now() - startTime).microseconds
        result.HasIssues = (len(result.IssuesFound) > 0)
        
        self.LogAnalysisResult(result)
        
        return result
