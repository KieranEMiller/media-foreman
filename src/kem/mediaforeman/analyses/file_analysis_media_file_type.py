import logging

from kem.mediaforeman.analyses.file_analysis_base import FileAnalysisBase
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from kem.mediaforeman.analyses.analysis_issue_type import AnalysisIssuePropertyType
from kem.mediaforeman.util.media_file_type_detector import MediaFileTypeDetector

_log = logging.getLogger()

class FileAnalysisMediaFileType(FileAnalysisBase):

    def __init__(self):
        pass
    
    def RequiresMediaFileType(self):
        return False
        
    def GetAnalysisType(self):
        return AnalysisType.FileMediaType

    def RunAnalysisOnFile(self, mediaFile):
        result = []
        
        detector = MediaFileTypeDetector()
        if(detector.IsExtensionOnPathAMatch(mediaFile.BasePath) == False):
            result.append(AnalysisIssuePropertyInvalid(
                mediaFile, AnalysisIssuePropertyType.FileType, detector.GetValidTypes(), mediaFile.GetName()
            ))
            
        return result