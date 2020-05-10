import os
from kem.mediaforeman.util.base_extension_detector import BaseExtensionDetector

class MediaRelatedFileTypeDetector(BaseExtensionDetector):

    def __init__(self):
        pass
        
    def GetValidTypes(self):
        return [".cue", ".m3u", ".log", ".jpg", ".jpeg"]