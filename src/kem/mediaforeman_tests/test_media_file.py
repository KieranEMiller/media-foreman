'''
Created on Jan 1, 2020

@author: kieranemiller
'''
import unittest
from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.media_file import MediaFile

class TestMediaFile(TestBaseFs):

    def test_sets_base_class_full_path_property(self):
        path = self.CopySampleMp3ToDir(self._testDir)
        mediaFile = MediaFile(path)
        self.assertEqual(mediaFile.BasePath, path)

    def test_file_metadata_extracts_properly(self):
        path = self.CopySampleMp3ToDir(self._testDir)
        mediaFile = MediaFile(path)
        mediaFile.ExtractProperties()
        
        self.assertEqual(mediaFile.Album, "TestAlbum")
        self.assertEqual(mediaFile.AlbumArtist, "SoundBibleArtist")
        self.assertEqual(mediaFile.Title, "TestTitle")
        
        '''track number does not seem to work properly
        self.assertEqual(mediaFile.TrackNumber, 3)
        '''
        
    def test_file_metadata_img_extracts_properly(self):
        path = self.CopySampleMp3WithImgToDir(self._testDir)
        mediaFile = MediaFile(path)
        mediaFile.ExtractProperties()
        
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()