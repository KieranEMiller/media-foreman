import os

from kem.mediaforeman.media_file import MediaFile
from kem.mediaforeman.media_base import MediaBase

class MediaCollection(MediaBase):

    def __init__(self, path):
        super(MediaCollection, self).__init__(path)
        self.MediaFiles = self.LoadContents(path)
        
    def LoadContents(self, path):

        mediaFiles = []
        for root, dirs, files in os.walk(path):
            for file in files:
                mediaFiles.append(MediaFile(file))

        return mediaFiles

