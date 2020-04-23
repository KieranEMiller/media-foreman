from mutagen.flac import FLAC
from kem.mediaforeman.metadata_parsers.base_parser import BaseParser
from kem.mediaforeman.metadata_parsers.metadata_result import MetadataResult
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
            
            '''
            result.AlbumArtist = self._eyed3Metadata.tag.album_artist
            if(result.AlbumArtist is None or result.AlbumArtist == ""):
                result.AlbumArtist = self._eyed3Metadata.tag.artist
            
            tracknum = self._eyed3Metadata.tag.track_num[0]
            if(str(tracknum).isdigit()):
                result.TrackNumber = tracknum
            '''
                
            result.BitRate = self._mutagenMeta.info.bitrate
            
            imgResult = self.ExtractImageProperties()
            result.CoverImgExists = imgResult.CoverImgExists
            result.CoverImgX = imgResult.CoverImgX
            result.CoverImgY = imgResult.CoverImgY
    
    def ExtractImageProperties(self):
        result = MetadataResult()
        result.CoverImgExists = False
        
        frontImg = [pic for pic in self._mutagenMeta.pictures if pic.type == PictureType.COVER_FRONT]
        if(frontImg != None and len(frontImg) > 0):
            result.CoverImgExists = True
            result.CoverImgX = frontImg[0].width
            result.CoverImgY = frontImg[0].height
        
        return result