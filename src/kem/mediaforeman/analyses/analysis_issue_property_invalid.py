from kem.mediaforeman.analyses.analysis_issue_base import AnalysisIssueBase

class AnalysisIssuePropertyInvalid(AnalysisIssueBase):

    def __init__(self, mediaFile, propertyName, expectedVal, actualVal):
        super(AnalysisIssuePropertyInvalid, self).__init__(mediaFile, propertyName, expectedVal, actualVal)        
        
    def GetText(self):
        return "Invalid Property: property '{}' with value '{}' was not correct, expected '{}'".format(
            self.IssueType, self.ActualVal, self.ExpectedVal
        )