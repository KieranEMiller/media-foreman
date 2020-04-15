import unittest
import uuid

from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.media_file import MediaFile
from kem.mediaforeman_tests.test_asset_constants import TestAssetConstants
import eyed3

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
            
    def test_save_metadata_works_for_all_regular_tag_data(self):
        path = self.CopySampleMp3ToDir()
        mediaFile = MediaFile(path)
        
        uniqueId = str(uuid.uuid1())
        mediaFile.Album = "Album {}".format(uniqueId)
        mediaFile.AlbumArtist = "AlbumArtist {}".format(uniqueId)
        mediaFile.Title = "Title {}".format(uniqueId)
        mediaFile.TrackNumber = 99
        mediaFile.SaveMetadata()
        
        secondLoad = MediaFile(path)
        self.assertEqual(secondLoad.AlbumArtist, mediaFile.AlbumArtist)
        self.assertEqual(secondLoad.Album, mediaFile.Album)
        self.assertEqual(secondLoad.Title, mediaFile.Title)
        self.assertEqual(secondLoad.TrackNumber, mediaFile.TrackNumber)
        
    def test_get_file_extension(self):
        path = self.CopySampleMp3ToDir()
        mediaFile = MediaFile(path)
        
        self.assertEqual(mediaFile.GetFileExtension(), ".mp3")
        
    def test_file_name_returns_full_name(self):
        path = self.CopySampleMp3ToDir(destFileName = "file_name.test")
        
        mediaFile = MediaFile(path)
        self.assertEqual(mediaFile.GetName(), "file_name.test")

    def test_file_name_without_extension(self):
        path = self.CopySampleMp3ToDir(destFileName = "file_name.test")

        mediaFile = MediaFile(path)
        
        self.assertEqual(mediaFile.GetNameNoExtension(), "file_name")
        
    def test_file_with_no_album_artist_uses_artist_as_backup(self):
        path = self.CopySampleMp3ToDir(testFile=TestAssetConstants.SAMPLE_MP3_NO_ALBUM_ARTIST_BUT_HAS_ARTIST)
        mediaFile = MediaFile(path)
        
        self.assertEqual(mediaFile.AlbumArtist, "Artist1")
        
    def test_save_metadata_saves_artist_to_album_artist_and_artist_fields(self):
        path = self.CopySampleMp3ToDir()
        mediaFile = MediaFile(path)
        
        uniqueId = str(uuid.uuid1())
        mediaFile.AlbumArtist = "AlbumArtist {}".format(uniqueId)
        mediaFile.SaveMetadata()
        
        metadata = eyed3.load(path)
        self.assertEqual(mediaFile.AlbumArtist, metadata.tag.album_artist)
        self.assertEqual(mediaFile.AlbumArtist, metadata.tag.artist)
        
    def flac_file_does_not_get_media_tags_loaded_properly(self):
        path = self.CopySampleMp3ToDir(testFile=TestAssetConstants.SAMPLE_FLAC)
        mediaFile = MediaFile(path)
        
        self.assertTrue(mediaFile.Album == "")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()