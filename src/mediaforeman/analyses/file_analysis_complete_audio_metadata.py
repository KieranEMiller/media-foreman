from mediaforeman.analyses.file_analysis_base import FileAnalysisBase
from mediaforeman.analyses.analysis_type import AnalysisType
from trace import CoverageResults
from mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from mediaforeman.analyses.analysis_issue_type import AnalysisIssuePropertyType

class FileAnalysisCompleteAudioMetadata(FileAnalysisBase):

    def __init__(self):
        pass
    
    def CanFix(self):
        return False
        
    def FixIssues(self):
        raise ValueError("unable to programatically fix missing audio metadata")
        
    def GetAnalysisType(self):
        return AnalysisType.FileCompleteAudioMetadata

    def RunAnalysisOnFile(self, mediaFile):
        results = []
        
        stringFieldsToTest = [
            ("Album", mediaFile.Album), 
            ("AlbumArtist", mediaFile.AlbumArtist), 
            ("Title", mediaFile.Title)
        ]
        
        for fieldName, fieldVal in stringFieldsToTest:
            if(fieldVal.strip() == ""):
                results.append(AnalysisIssuePropertyInvalid(
                    mediaFile, AnalysisIssuePropertyType.MetadataFieldEmpty, "NOT_EMPTY", fieldName
                ))
        
        if(mediaFile.TrackNumber <= 0):
            results.append(AnalysisIssuePropertyInvalid(
                mediaFile, AnalysisIssuePropertyType.TrackNumberInvalid, "1 or greater", mediaFile.TrackNumber
            ))
            
        return results