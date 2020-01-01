import os

from kem.mediaforeman.media_file import MediaFile
from kem.mediaforeman.media_base import MediaBase

class MediaCollection(MediaBase):

    def __init__(self, path):
        super(MediaCollection, self).__init__(path)
        self._mediaFiles = self.LoadContents(path)
        
    def LoadContents(self, path):

        files = []
        for file in os.walk(path):
            files.append(MediaFile(file))

        return files

