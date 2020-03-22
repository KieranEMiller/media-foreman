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
    
    def IsCollectionAnalysis(self):
        return False
    
    def IsFileAnalysis(self):
        return True

    '''not abstract here since this method is not overridden
    by subclasses; this base method handles execution for all subclasses'''
    def RunAnalysisOnCollection(self, mediaColl):
        results = []
        for mediaFile in mediaColl.MediaFiles:
            if(self.ShouldRun(mediaFile) == True):
                results.extend(self.RunAnalysisOnFile(mediaFile))
        
        return results

    '''
    def ShouldRun(self, media):
        if(self.RequiresMediaFileType() == True):
            detector = MediaFileTypeDetector()
            if(detector.IsMediaFileType(media.BasePath) == False):
                return False
            
        return True
    '''