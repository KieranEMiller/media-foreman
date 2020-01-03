'''
Created on Dec 30, 2019

@author: kieranemiller
'''
from kem.mediaforeman.analyses.file_analysis_base import FileAnalysisBase
from kem.mediaforeman.analyses.analysis_type import AnalysisType

class FileAnalysisValidImage(FileAnalysisBase):

    def __init__(self, params):
        pass
        
    def GetAnalysisType(self):
        return AnalysisType.FileValidImage

    def RunAnalysisOnFile(self, mediaFile):
        pass
    