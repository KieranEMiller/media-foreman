import os

class MediaFile(object):

    def __init__(self, path):
        self._filePath = path
        
    def IsMedia(self):
        '''if the extension is one of a set of types
        //currently just supporting audio'''
        audioTypes = ['mp3', 'wav', 'ogg', 'mp4', 'flac']
        return True

    def ExtractProperties(self):
        '''
        //get all properties as a dictionary
        //need a third party library here
        '''
        pass


