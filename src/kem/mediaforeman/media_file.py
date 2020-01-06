import os
import eyed3
from PIL import Image
from io import BytesIO

from kem.mediaforeman.media_base import MediaBase

class MediaFile(MediaBase):

    def __init__(self, path):
        super(MediaFile, self).__init__(path)
        
        '''alphanumerical metadata'''
        self.Album = ""
        self.AlbumArtist = ""
        self.Title = ""
        self.TrackNumber = -1
        
        '''image metadata'''
        self.CoverImgExists = False
        self.CoverImgX = -1
        self.CoverImgY = -1
        
        self.ExtractProperties()
        
    def ExtractProperties(self):
        metadata = eyed3.load(self.BasePath)

        self.Album = metadata.tag.album
        self.AlbumArtist = metadata.tag.album_artist
        self.Title = metadata.tag.title
        self.TrackNumber = metadata.tag.track_num
        
        self.ExtractImageProperties(metadata)
        
    def ExtractImageProperties(self, metadata):
        '''picture type here represents the type of image embedded in the file
             3: Front Cover, 
             4: Back Cover
             0: other
        '''
        if(len(metadata.tag.images) > 0):
            '''currently only support and care about images on the front cover'''
            frontCoverImg = list(filter(lambda i: i.picture_type == 3, metadata.tag.images))
        
            if(len(frontCoverImg) > 0):
                rawBytes =  bytearray(frontCoverImg[0].image_data)
                img = Image.open(BytesIO(rawBytes))
                self.CoverImgExists = True
                
                width, height = img.size
                self.CoverImgX = width
                self.CoverImgY = height
                
                img.close()

