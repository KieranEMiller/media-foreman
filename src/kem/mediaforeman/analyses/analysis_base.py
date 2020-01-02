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
    
    def RunAnalysis(self, runAgainst):
        startTime = datetime.datetime.now()
        print("running analysis '{}' against {}".format(self.GetAnalysisType(), type(runAgainst)))
        
        result = AnalysisResult()
        result.AnalysisType = self.GetAnalysisType()
        
        if(isinstance(runAgainst, MediaCollection)):
            result.IssuesFound = self.RunAnalysisOnCollection(runAgainst)
        
        elif(isinstance(runAgainst, MediaFile)):
            result.IssuesFound = self.RunAnalysisOnFile(runAgainst)
        
        else:
            raise ValueError("unknown run analysis parameter")
            
        result.ElapsedInMicroSecs = datetime.datetime.now() - startTime
        return result
