from kem.mediaforeman.analyses.file_analysis_base import FileAnalysisBase
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from kem.mediaforeman.analyses.analysis_issue_type import AnalysisIssuePropertyType

class FileAnalysisTrackNamingConvention(FileAnalysisBase):

    def __init__(self):
        pass
        
    def GetAnalysisType(self):
        return AnalysisType.FileTrackNamingConvention

    def RunAnalysisOnFile(self, mediaFile):
        results = []
        
        expectedName = "{0:02d} - {} - {}".format(
            mediaFile.TrackNumber,
            mediaFile.Album, 
            mediaFile.AlbumArtist
        )
        actualName = mediaFile.GetName()
        
        if(expectedName != actualName):
            results.append(AnalysisIssuePropertyInvalid(
                mediaFile, 
                AnalysisIssuePropertyType.TrackNamingConvention, 
                expectedName, 
                actualName
            ))
        