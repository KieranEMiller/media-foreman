'''
Created on Dec 30, 2019

@author: kieranemiller
'''
import datetime
from abc import abstractmethod

from kem.mediaforeman.media_collection import MediaCollection
from kem.mediaforeman.media_file import MediaFile

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
        if(isinstance(runAgainst, MediaCollection)):
            return self.RunAnalysisOnCollection(runAgainst)
        
        elif(isinstance(runAgainst, MediaFile)):
            return self.RunAnalysisOnFile(runAgainst)
        
        else:
            raise ValueError("unknown run analysis parameter")
            
        self.ElapsedTime = datetime.datetime.now() - startTime
        print("analysis '{}' completed in {}us".format(self.ElapsedTime.microseconds))
