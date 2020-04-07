from kem.mediaforeman.analyses.analysis_issue_base import AnalysisIssueBase

class AnalysisIssueMediaSkipped(AnalysisIssueBase):

    def __init__(self, mediaFile, reason):
        self.MediaFile = mediaFile
        self.ErrorMsg = reason
        
    def GetText(self):
        return "Media at '{}' skipped: {}".format(
            self.MediaFile.BasePath, self.ErrorMsg
        )