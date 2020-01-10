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
        
        self.assertEqual(mediaFile.Album, "TestAlbum")
        self.assertEqual(mediaFile.AlbumArtist, "SoundBibleArtist")
        self.assertEqual(mediaFile.Title, "TestTitle")
        self.assertEqual(mediaFile.TrackNumber, 3)
        
    def test_file_metadata_img_extracts_properly(self):
        path = self.CopySampleMp3ToDir(testFile = "./assets/sample_mp3_with_img_below_size_minimums.mp3")
        mediaFile = MediaFile(path)
        
        self.assertTrue(mediaFile.CoverImgExists)
        self.assertGreater(mediaFile.CoverImgX, 0)
        self.assertGreater(mediaFile.CoverImgY, 0)
        
    def test_file_metadata_shows_no_cover_img_when_none_present(self):
        path = self.CopySampleMp3ToDir(self._testDir)
        mediaFile = MediaFile(path)

        self.assertFalse(mediaFile.CoverImgExists)
        
    def test_audio_bitrate_and_duration(self):
        path = self.CopySampleMp3ToDir(self._testDir)
        mediaFile = MediaFile(path)
        
        self.assertGreater(mediaFile.Duration, 3)
        self.assertLess(mediaFile.Duration, 4)
        self.assertEqual(mediaFile.BitRate, 172)
        
        
    def test_mp3_with_no_property_tags_does_not_error_out_uses_defaults(self):
        path = self.CopySampleMp3ToDir(testFile = "./assets/sample_mp3_with_no_metadata.mp3")
        
        try:
            mediaFile = MediaFile(path)
        
        except Exception:
            self.fail("MediaFile ctor failed on tag with no metadata")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()