from mutagen.flac import FLAC
from kem.mediaforeman.metadata_parsers.base_parser import BaseParser
from kem.mediaforeman.metadata_parsers.metadata_result import MetadataResult

class FlacParser(BaseParser):

    def __init__(self, path):
        super(FlacParser, self).__init__(path)
        
        self._mutagenMeta = None
    
    def ExtractProperties(self):
        self._mutagenMeta = FLAC(self.Path)
        
        result = MetadataResult()
        if(self._eyed3Metadata.tag != None):
            result.Album = self._eyed3Metadata.tag.album
            result.Title = self._eyed3Metadata.tag.title
            
            result.AlbumArtist = self._eyed3Metadata.tag.album_artist
            if(result.AlbumArtist is None or result.AlbumArtist == ""):
                result.AlbumArtist = self._eyed3Metadata.tag.artist
            
            tracknum = self._eyed3Metadata.tag.track_num[0]
            if(str(tracknum).isdigit()):
                result.TrackNumber = tracknum
            
            imgResult = self.ExtractImageProperties()
            result.CoverImgExists = imgResult.CoverImgExists
            result.CoverImgX = imgResult.CoverImgX
            result.CoverImgY = imgResult.CoverImgY
    
    def ExtractImageProperties(self):
        pass