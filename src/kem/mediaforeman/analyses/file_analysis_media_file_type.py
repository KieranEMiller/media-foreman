'''
Created on Dec 30, 2019

@author: kieranemiller
'''
from kem.mediaforeman.analyses.file_analysis_base import FileAnalysisBase
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid

class FileAnalysisMediaFileType(FileAnalysisBase):

    def __init__(self):
        pass
        
    def GetAnalysisType(self):
        return AnalysisType.FileCompleteAudioMetadata

    def RunAnalysisOnFile(self, mediaFile):
        result = []
        
        '''TODO: expand to include additional types.  just audio types for now'''
        validTypes = ["mp3", "flac", "wav", "ogg", "mp4"]
        
        for validType in validTypes:
            if(not mediaFile.GetFileName().endswith(validType)):
                result.append(AnalysisIssuePropertyInvalid("Invalid Media File Type", validTypes, mediaFile.GetFileName()))
                break
            
        return result