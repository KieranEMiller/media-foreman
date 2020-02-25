from abc import abstractmethod

from kem.mediaforeman.analyses.analysis_base import AnalysisBase
from kem.mediaforeman.media_file import MediaFile
from kem.mediaforeman.util.media_file_type_detector import MediaFileTypeDetector

class FileAnalysisBase(AnalysisBase):

    def __init__(self, params):
        pass
    
    @abstractmethod
    def RequiresMediaFileType(self):
        return True
    
    @abstractmethod
    def GetAnalysisType(self):
        pass

    @abstractmethod
    def RunAnalysisOnFile(self, mediaFile):
        pass
    
    '''not abstract here since this method is not overridden
    but subclasses'''
    def RunAnalysisOnCollection(self, mediaColl):
        results = []
        for mediaFile in mediaColl.MediaFiles:
            results.extend(self.RunAnalysisOnFile(mediaFile))
        
        return results

    def ShouldRun(self, mediaFile):
        if(self.RequiresMediaFileType() == True):
            detector = MediaFileTypeDetector()
            if(detector.IsMediaFileType(mediaFile.BasePath) == False):
                return False
            
        return True