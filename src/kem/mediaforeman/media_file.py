import os
import eyed3
from PIL import Image

from kem.mediaforeman.media_base import MediaBase

class MediaFile(MediaBase):

    def __init__(self, path):
        super(MediaFile, self).__init__(path)
        
        self.Album = ""
        self.AlbumArtist = ""
        self.Title = ""
        self.TrackNumber = -1
        
    def ExtractProperties(self):
        metadata = eyed3.load(self.BasePath)

        self.Album = metadata.tag.album
        self.AlbumArtist = metadata.tag.album_artist
        self.Title = metadata.tag.title
        self.TrackNumber = metadata.tag.track_num
        
        self.ExtractImage(metadata)

    def ExtractImage(self, metadata):
        print("checking image with {} imgs".format(len(metadata.tag.images)))
        for img in metadata.tag.images:

            '''print("found image, type {}, picture type {}, desc {}".format(img.mime_type, img.picture_type, img.description))'''
            bytes = bytearray(img.image_data)
            
            '''
            with open("test.png", "wb") as outfile:
                outfile.write(bytes)
            '''

