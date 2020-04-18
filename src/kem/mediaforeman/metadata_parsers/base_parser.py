from abc import abstractmethod
import os
import eyed3
from PIL import Image
from io import BytesIO

class BaseParser(object):

    def __init__(self, path):
        self.Path = path
        
    @abstractmethod
    def ExtractProperties(self):
        pass
    
    @abstractmethod
    def ExtractImageProperties(self):
        pass
    
    @abstractmethod
    def SaveMetadata(self, mediaFle):
        pass
    
    def GetImageSizeFromByteArray(self, rawBytes):
        img = Image.open(BytesIO(rawBytes))
        width, height = img.size
        img.close()
        return width, height