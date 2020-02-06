'''
Created on Dec 30, 2019

@author: kieranemiller
'''
from abc import abstractmethod

from kem.mediaforeman.analyses.analysis_base import AnalysisBase
from kem.mediaforeman.media_file import MediaFile

class FileAnalysisBase(AnalysisBase):

    def __init__(self, params):
        pass
        
    @abstractmethod
    def GetAnalysisType(self):
        pass

    @abstractmethod
    def RunAnalysisOnFile(self, mediaFile):
        pass
    
    def RunAnalysisOnCollection(self, mediaColl):
        
        results = []
        for mediaFile in mediaColl.MediaFiles:
            results.extend(self.RunAnalysisOnFile(mediaFile))
        
        return results