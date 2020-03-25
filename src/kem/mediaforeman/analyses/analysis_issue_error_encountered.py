from kem.mediaforeman.analyses.analysis_issue_base import AnalysisIssueBase

class AnalysisIssueErrorEncountered(AnalysisIssueBase):

    def __init__(self, mediaFile, errMsg):
        self.MediaFile = mediaFile
        self.ErrorMsg = errMsg
        
    def GetText(self):
        return "Error encountered processing media at '{}': {}".format(
            self.MediaFile.BasePath, self.ErrorMsg
        )