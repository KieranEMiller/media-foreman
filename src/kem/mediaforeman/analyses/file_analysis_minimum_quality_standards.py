'''
Created on Dec 30, 2019

@author: kieranemiller
'''
from kem.mediaforeman.analyses.file_analysis_base import FileAnalysisBase
from kem.mediaforeman.analyses.analysis_type import AnalysisType

class FileAnalysisMinimumQualityStandards(FileAnalysisBase):

    def __init__(self, params):
        self.MinBitRate = 256
        self.AllowLossy = true

        '''other properties for future enhancement'''
        '''currently unused '''
        self.MinNumChannels = -1
        self.MinFreq = -1
        
    def GetAnalysisType(self):
        return AnalysisType.FileMinimumQualityStandards

    def RunAnalysisOnFile(self, mediaFile):
        pass
    