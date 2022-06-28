from abc import abstractmethod

from mediaforeman.analyses.analysis_base import AnalysisBase
from mediaforeman.media_file import MediaFile
from mediaforeman.util.media_file_type_detector import MediaFileTypeDetector

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
    
    @abstractmethod
    def FixIssues(self):
        pass
    
    def IsCollectionAnalysis(self):
        return False
    
    def IsFileAnalysis(self):
        return True

    def RunAnalysisOnCollection(self, mediaColl):
        pass

    