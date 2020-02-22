from kem.mediaforeman.analyses.file_analysis_base import FileAnalysisBase
from kem.mediaforeman.analyses.analysis_type import AnalysisType

class FileAnalysisTrackNamingConvention(FileAnalysisBase):

    def __init__(self):
        pass
        
    def GetAnalysisType(self):
        return AnalysisType.FileTrackNamingConvention

    def RunAnalysisOnFile(self, mediaFile):
        results = []
        
        
        