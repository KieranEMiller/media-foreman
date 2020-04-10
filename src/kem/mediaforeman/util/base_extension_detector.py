import os
from abc import abstractmethod

class BaseExtensionDetector(object):

    def __init__(self):
        pass
        
    @abstractmethod
    def GetValidTypes(self):
        pass
    
    def IsValid(self, path):
        #extension = os.path.splitext(path)[1].lower()
        validTypes = self.GetValidTypes()
        match = [extension for extension in validTypes if path.endswith(extension.lower())]
        
        return len(match) != 0