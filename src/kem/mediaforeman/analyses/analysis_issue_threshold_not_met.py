from kem.mediaforeman.analyses.analysis_issue_base import AnalysisIssueBase

class AnalysisIssueThresholdNotMet(AnalysisIssueBase):

    def __init__(self, propertyName, thresholdVal, actualVal):
        super(AnalysisIssueThresholdNotMet, self).__init__(propertyName, thresholdVal, actualVal)        
        
    def GetText(self):
        return "Threshold Not Met: property '{}' with value '{}' did not meet the configured threshold of '{}'".format(
            self.PropertyName, self.ActualVal, self.ExpectedVal
        )