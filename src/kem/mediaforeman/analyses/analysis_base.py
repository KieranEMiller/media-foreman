'''
Created on Dec 30, 2019

@author: kieranemiller
'''
import datetime
from abc import abstractmethod

from kem.mediaforeman.media_collection import MediaCollection
from kem.mediaforeman.media_file import MediaFile
from kem.mediaforeman.analyses.analysis_result import AnalysisResult

class AnalysisBase(object):

    def __init__(self, params):
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
    
    def RunAnalysis(self, media):
        startTime = datetime.datetime.now()
        print("running analysis '{}' against {}".format(self.GetAnalysisType(), type(media)))
        
        result = AnalysisResult()
        result.AnalysisType = self.GetAnalysisType()
        result.Media = media

        if(isinstance(media, MediaCollection)):
            result.IssuesFound = self.RunAnalysisOnCollection(media)
        
        elif(isinstance(media, MediaFile)):
            result.IssuesFound = self.RunAnalysisOnFile(media)
        
        else:
            raise ValueError("unknown run analysis parameter")
            
        result.ElapsedInMicroSecs = (datetime.datetime.now() - startTime).microseconds
        return result
