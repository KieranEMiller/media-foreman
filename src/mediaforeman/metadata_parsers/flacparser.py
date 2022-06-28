from mutagen.flac import FLAC
from mediaforeman.metadata_parsers.base_parser import BaseParser
from mediaforeman.metadata_parsers.metadata_result import MetadataResult
from mutagen.id3._specs import PictureType

class FlacParser(BaseParser):

    def __init__(self, path):
        super(FlacParser, self).__init__(path)
        
        self._mutagenMeta = None
    
    def ExtractProperties(self):
        self._mutagenMeta = FLAC(self.Path)
        
        result = MetadataResult()
        if(self._mutagenMeta != None):
            
            result.Album = self._mutagenMeta["album"][0]
            result.Title = self._mutagenMeta["title"][0]
            result.AlbumArtist = self._mutagenMeta["artist"][0]
            
            if(str(self._mutagenMeta["tracknumber"][0]).isdigit()):
                result.TrackNumber = int(self._mutagenMeta["tracknumber"][0])
                
            result.BitRate = self._mutagenMeta.info.bitrate
            
            imgResult = self.ExtractImageProperties()
            result.CoverImgExists = imgResult.CoverImgExists
            result.CoverImgX = imgResult.CoverImgX
            result.CoverImgY = imgResult.CoverImgY
        
        return result
    
    def ExtractImageProperties(self):
        result = MetadataResult()
        result.CoverImgExists = False
        
        frontImg = [pic for pic in self._mutagenMeta.pictures if pic.type == PictureType.COVER_FRONT]
        if(frontImg != None and len(frontImg) > 0):
            result.CoverImgExists = True
            width, height = self.GetImageSizeFromByteArray(frontImg[0].data)
            result.CoverImgX = width
            result.CoverImgY = height
        
        return result