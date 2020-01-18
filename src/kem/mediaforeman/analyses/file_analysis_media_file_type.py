'''
Created on Dec 30, 2019

@author: kieranemiller
'''
import logging

from kem.mediaforeman.analyses.file_analysis_base import FileAnalysisBase
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from kem.mediaforeman.analyses.analysis_issue_type import AnalysisIssuePropertyType

_log = logging.getLogger()

class FileAnalysisMediaFileType(FileAnalysisBase):

    def __init__(self):
        pass
        
    def GetAnalysisType(self):
        return AnalysisType.FileMediaType

    def RunAnalysisOnFile(self, mediaFile):
        result = []
        
        '''TODO: expand to include additional types.  just audio types for now'''
        validTypes = ["mp3", "flac", "wav", "ogg", "mp4"]
        
        match = [extension for extension in validTypes if mediaFile.GetFileName().endswith(extension.lower())]
        if(len(match) == 0):
            result.append(AnalysisIssuePropertyInvalid(
                mediaFile, AnalysisIssuePropertyType.FileType, validTypes, mediaFile.GetFileName()
            ))
            
        return result