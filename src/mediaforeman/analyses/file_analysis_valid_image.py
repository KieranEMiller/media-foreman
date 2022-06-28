from mediaforeman.analyses.file_analysis_base import FileAnalysisBase
from mediaforeman.analyses.analysis_type import AnalysisType
from mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from mediaforeman.analyses.analysis_issue_threshold_not_met import AnalysisIssueThresholdNotMet
from mediaforeman.analyses.analysis_issue_type import AnalysisIssuePropertyType

class FileAnalysisValidImage(FileAnalysisBase):

    def __init__(self):
        self._requiredXandYPixelLength = 256
        
    def GetAnalysisType(self):
        return AnalysisType.FileValidImage

    def RunAnalysisOnFile(self, mediaFile):
        results = []
        
        if(mediaFile.CoverImgExists == False):
            results.append(AnalysisIssuePropertyInvalid(
                mediaFile, AnalysisIssuePropertyType.CoverImageExists, True, mediaFile.CoverImgExists
            ))

        if(mediaFile.CoverImgX < self._requiredXandYPixelLength or mediaFile.CoverImgX <= 0):
            results.append(AnalysisIssueThresholdNotMet(
                mediaFile, AnalysisIssuePropertyType.CoverImageXDimensions, self._requiredXandYPixelLength, mediaFile.CoverImgX
            ))
            
        if(mediaFile.CoverImgY < self._requiredXandYPixelLength or mediaFile.CoverImgY <= 0):
            results.append(AnalysisIssueThresholdNotMet(
                mediaFile, AnalysisIssuePropertyType.CoverImageYDimensions, self._requiredXandYPixelLength, mediaFile.CoverImgY
            ))

        return results
    
    def CanFix(self):
        return False
    
    def FixIssues(self, media):
        raise ValueError("unable to programatically fix image issues")
    