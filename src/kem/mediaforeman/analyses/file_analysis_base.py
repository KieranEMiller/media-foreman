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

    def RunAnalysisOnCollection(self, mediaColl):
        pass
