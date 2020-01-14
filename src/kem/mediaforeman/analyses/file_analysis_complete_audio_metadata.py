'''
Created on Dec 30, 2019

@author: kieranemiller
'''
from kem.mediaforeman.analyses.file_analysis_base import FileAnalysisBase
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from trace import CoverageResults
from kem.mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid

class FileAnalysisCompleteAudioMetadata(FileAnalysisBase):

    def __init__(self):
        pass
        
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
                results.append(AnalysisIssuePropertyInvalid("Metadata Field Empty", "NOT_EMPTY", fieldName))
        
        if(mediaFile.TrackNumber <= 0):
            results.append(AnalysisIssuePropertyInvalid("Metadata Field Empty", "1 or greater", mediaFile.TrackNumber))
            
        return results