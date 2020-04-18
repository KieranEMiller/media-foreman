import os
import eyed3
from PIL import Image
from io import BytesIO
import logging

from kem.mediaforeman.media_base import MediaBase
from kem.mediaforeman.metadata_parsers.parser_factory import ParserFactory

_log = logging.getLogger()

class MediaFile(MediaBase):

    def __init__(self, path = None):
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
        
        '''other properties '''
        self.Duration = -1
        self.BitRate = -1
        
        self._parser = None
        if(path != None):
            self._parser = ParserFactory().GetParserFromFilePath(path)
            if(self._parser != None):
                result = self._parser.ExtractProperties()
                self.SetPropertiesFromParserResult(result)
        
    def GetName(self):
        return os.path.basename(self.BasePath)
    
    def GetNameNoExtension(self):
        '''have to usebasename because the first part of the splitext method
        returns the full path to the file, not just the name'''
        return os.path.basename(os.path.splitext(self.BasePath)[0])
    
    def GetFileExtension(self):
        '''splitext returns a tuple filename, fileext, so index 1 
           is the extension'''
        return os.path.splitext(self.BasePath)[1]
    
    def SetPropertiesFromParserResult(self, parserResult):
        self.Album = parserResult.Album
        self.AlbumArtist = parserResult.AlbumArtist
        self.Title = parserResult.Title
        self.TrackNumber = parserResult.TrackNumber
        self.CoverImgExists = parserResult.CoverImgExists
        self.CoverImgX = parserResult.CoverImgX
        self.CoverImgY = parserResult.CoverImgY
        self.Duration = parserResult.Duration
        self.BitRate = parserResult.BitRate

    '''only saves metadata, not images (for now) '''
    def SaveMetadata(self):

        _log.info("saving metadata for {}, artist: {}, album: {}, title: {}, track: {}".format(
            self.BasePath, self.AlbumArtist, self.Album, self.Title, self.TrackNumber
        ))
        
        self._parser.SaveMetadata(self)