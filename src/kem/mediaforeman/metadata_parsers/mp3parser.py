from kem.mediaforeman.metadata_parsers.base_parser import BaseParser
import os
import eyed3
from kem.mediaforeman.metadata_parsers.metadata_result import MetadataResult

class Mp3Parser(BaseParser):

    def __init__(self, path):
        super(self, path).__init__(path)
        
        '''do not load the file in the ctor, rather wait for the call to 
        Extract Properties'''
        self._eyed3Metadata = None
        
    def ExtractProperties(self):
        self._eyed3Metadata = eyed3.load(self.Path)
        
        '''TODO: could not open or load tags, what to do here?'''
        if(self._eyed3Metadata == None):
            return None

        result = MetadataResult()
        if(self._eyed3Metadata.tag != None):
            result.Album = self._eyed3Metadata.tag.album
            result.Title = self._eyed3Metadata.tag.title
            
            result.AlbumArtist = self._eyed3Metadata.tag.album_artist
            if(result.AlbumArtist is None or self.AlbumArtist == ""):
                result.AlbumArtist = self._eyed3Metadata.tag.artist
            
            tracknum = self._eyed3Metadata.tag.track_num[0]
            if(str(tracknum).isdigit()):
                result.TrackNumber = tracknum
            
            imgResult = result.ExtractImageProperties()
            result.CoverImgExists = imgResult.CoverImgExists
            result.CoverImgX = imgResult.CoverImgX
            result.CoverImgY = imgResult.CoverImgY
        
        if(self._eyed3Metadata.info != None):
            result.Duration = self._eyed3Metadata.info.time_secs

            bitRateVrb, bitRateVal = self._eyed3Metadata.info.bit_rate
            result.BitRate = bitRateVal
            
        return result
            
    def ExtractImageProperties(self):
        '''picture type here represents the type of image embedded in the file
             3: Front Cover, 
             4: Back Cover
             0: other
        '''
        imgResult = MetadataResult()
        imgResult.CoverImgExists = False
        
        if(len(self._eyed3Metadata.tag.images) > 0):
            '''currently only support and care about images on the front cover'''
            frontCoverImg = list(filter(lambda i: i.picture_type == 3, self._eyed3Metadata.tag.images))
        
            if(len(frontCoverImg) > 0):
                rawBytes =  bytearray(frontCoverImg[0].image_data)
                width, height = self.GetImageSizeFromByteArray(rawBytes)
                imgResult.CoverImgExists = True
                imgResult.CoverImgX = width
                imgResult.CoverImgY = height
        
        return imgResult
                