
class MetadataResult(object):

    def __init__(self):
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
    
    