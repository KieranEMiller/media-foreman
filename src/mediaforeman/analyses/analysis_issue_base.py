import abc
from abc import abstractmethod

class AnalysisIssueBase(object):

    def __init__(self, mediaFile, issueType, expectedVal, actualVal):
        self.MediaFile = mediaFile
        self.IssueType = issueType
        self.ExpectedVal = expectedVal
        self.ActualVal = actualVal
    
    @abstractmethod
    def GetText(self):
        raise NotImplemented()