from kem.mediaforeman.metadata_parsers.base_parser import BaseParser
import os
import eyed3
from PIL import Image
from io import BytesIO

class Mp3Parser(BaseParser):

    def __init__(self, path):
        super(self, path).__init__(path)
        
    def ExtractProperties(self):
        metadata = eyed3.load(self.BasePath)
        
        if(metadata == None):
            return

        if(metadata.tag != None):
            self.Album = metadata.tag.album
            self.Title = metadata.tag.title
            
            self.AlbumArtist = metadata.tag.album_artist
            if(self.AlbumArtist is None or self.AlbumArtist == ""):
                self.AlbumArtist = metadata.tag.artist
            
            tracknum = metadata.tag.track_num[0]
            if(str(tracknum).isdigit()):
                self.TrackNumber = tracknum
            
            self.ExtractImageProperties(metadata)
        
        if(metadata.info != None):
            self.Duration = metadata.info.time_secs

            bitRateVrb, bitRateVal = metadata.info.bit_rate
            self.BitRate = bitRateVal
            
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