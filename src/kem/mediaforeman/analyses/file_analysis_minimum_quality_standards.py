'''
Created on Dec 30, 2019

@author: kieranemiller
'''
import os

from kem.mediaforeman.analyses.file_analysis_base import FileAnalysisBase
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.analyses.analysis_result import AnalysisResult
from kem.mediaforeman.analyses.analysis_issue_threshold_not_met import AnalysisIssueThresholdNotMet
from kem.mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid

class FileAnalysisMinimumQualityStandards(FileAnalysisBase):

    def __init__(self, params):
        self.MinBitRate = 256
        self.AllowLossy = True

        '''other properties for future enhancement'''
        '''currently unused '''
        self.MinNumChannels = -1
        self.MinFreq = -1
        
    def GetAnalysisType(self):
        return AnalysisType.FileMinimumQualityStandards

    def RunAnalysisOnFile(self, mediaFile):
        issues = []
        if(mediaFile.BitRate < self.MinBitRate):
            issues.append(AnalysisIssueThresholdNotMet("BitRate", self.MinBitRate, mediaFile.BitRate))
            
        if(mediaFile.AllowLossy == False):
            '''
            for now just go based on extension even though this is not an accurate way
            to determine compression
            TODO: can FLAC be lossy?
            '''
            lossyTypes = ['.mp3', '.mp4' ]
            for lossyType in lossyTypes:
                if(mediaFile.GetFileName().endswith(lossyType)):
                    issues.append(AnalysisIssuePropertyInvalid("AllowLossy", True, self.AllowLossy))
                    break
            
        return issues
    