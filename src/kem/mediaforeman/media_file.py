import os
from kem.mediaforeman.media_base import MediaBase

class MediaFile(MediaBase):

    def __init__(self, path):
        super(MediaFile, self).__init__(path)
        
    def ExtractProperties(self):
        '''
        //get all properties as a dictionary
        //need a third party library here
        '''
        pass

    def ExtractImage(self):
        '''do we need temp file system space/loc for this?'''
        pass

    
