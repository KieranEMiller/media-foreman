'''
Created on Dec 30, 2019

@author: kieranemiller
'''
from kem.mediaforeman.analyses.file_analysis_base import FileAnalysisBase
from kem.mediaforeman.analyses.analysis_type import AnalysisType

class FileAnalysisMediaFileType(FileAnalysisBase):

    def __init__(self):
        pass
        
    def GetAnalysisType(self):
        return AnalysisType.FileCompleteAudioMetadata

    def RunAnalysisOnFile(self, mediaFile):
        '''TODO: expand to include additional types.  just audio types for now'''
        validTypes = ["mp3", "flac", "wav", "ogg", "mp4"]
        
        '''check if the mediaFile extension ends in one of the above'''