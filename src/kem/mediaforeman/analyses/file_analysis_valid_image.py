'''
Created on Dec 30, 2019

@author: kieranemiller
'''
from kem.mediaforeman.analyses.file_analysis_base import FileAnalysisBase
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from kem.mediaforeman.analyses.analysis_issue_threshold_not_met import AnalysisIssueThresholdNotMet

class FileAnalysisValidImage(FileAnalysisBase):

    def __init__(self, params):
        self._requiredXandYPixelLength = 256
        
    def GetAnalysisType(self):
        return AnalysisType.FileValidImage

    def RunAnalysisOnFile(self, mediaFile):
        results = []
        
        if(mediaFile.CoverImgExists == False):
            results.append(AnalysisIssuePropertyInvalid(
                "Cover Image Exists", True, mediaFile.CoverImgExists
            ))

        if(mediaFile.CoverImgX < self._requiredXandYPixelLength or mediaFile.CoverImgX <= 0):
            results.append(AnalysisIssueThresholdNotMet(
                "Cover Image X Dimensions", self._requiredXandYPixelLength, mediaFile.CoverImgX
            ))
            
        if(mediaFile.CoverImgY < self._requiredXandYPixelLength or mediaFile.CoverImgY <= 0):
            results.append(AnalysisIssueThresholdNotMet(
                "Cover Image Y Dimensions", self._requiredXandYPixelLength, mediaFile.CoverImgY
            ))

        return results