import os
from kem.mediaforeman.util.base_extension_detector import BaseExtensionDetector

class MediaFileTypeDetector(BaseExtensionDetector):

    def __init__(self):
        pass
        
    def GetValidTypes(self):
        return ["mp3", "flac", "wav", "ogg", "mp4"]
    