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
        return 
    
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

        try:
            if(isinstance(media, MediaCollection)):
                result.IssuesFound = self.RunAnalysisOnCollection(media)
            
            elif(isinstance(media, MediaFile)):
                result.IssuesFound = self.RunAnalysisOnFile(media)
            
            else:
                raise ValueError("unknown run analysis media parameter")
            
        except:
            _log.error("failed to run analysis on media at path {}".format(media.BasePath))
            
        result.ElapsedInMicroSecs = (datetime.datetime.now() - startTime).microseconds
        result.HasIssues = (len(result.IssuesFound) > 0)
        
        self.LogAnalysisResult(result)
        
        return result
