import abc
from abc import abstractmethod

class AnalysisIssueBase(object):

    def __init__(self, propertyName, expectedVal, actualVal):
        self.PropertyName = propertyName
        self.ExpectedVal = expectedVal
        self.ActualVal = actualVal
    
    @abstractmethod
    def GetText(self):
        raise NotImplemented()