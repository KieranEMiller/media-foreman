import os
from abc import abstractmethod

class MediaBase(object):

    def __init__(self, path):
        self.BasePath = path
        
        if(path != None and os.path.exists(path)):
            self.ParentDirectory = os.path.abspath(os.path.join(path, os.pardir))
            
    @abstractmethod
    def GetName(self):
        pass
    
    def GetParentDirPath(self):
        return os.path.dirname(self.BasePath)