from abc import abstractmethod

class BaseParser(object):

    def __init__(self, path):
        self.Path = path
        
    @abstractmethod
    def ExtractProperties(self):
        pass
    
    @abstractmethod
    def ExtractImageProperties(self):
        pass