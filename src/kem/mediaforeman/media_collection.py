import os

from kem.mediaforeman.media_file import MediaFile

class MediaCollection(object):

    def __init__(self, path):
        self._basePath = path
        self._mediaFiles = self.LoadContents(path)
        
    def LoadContents(self):

        files = []
        for file in os.walk(self._basePath):
            files.append(MediaFile(file))

        return files

