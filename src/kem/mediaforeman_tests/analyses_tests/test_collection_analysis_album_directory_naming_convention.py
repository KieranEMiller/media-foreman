import unittest
import shutil

from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.media_collection import MediaCollection
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.media_file import MediaFile
from kem.mediaforeman.analyses.collection_analysis_album_directory_naming_convention import CollectionAnalysisAlbumDirectoryNamingConvention

class TestCollectionAnalysisAlbumDirectoryNamingConvention(TestBaseFs):

    def test_album_directory_naming_convention_correct_returns_no_issues(self):
        
        ARTIST_NAME = "ArtistTest"
        ALBUM_NAME="Album01Test"
        
        albumPath = self.CreateSubDirectory(dirName = "{} - {}".format(ARTIST_NAME, ALBUM_NAME))

        for i in range(0, 4):
            filePath = self.CopySampleMp3ToDir(testDir=albumPath)
            mediaFile = MediaFile(filePath)
            mediaFile.Album = ALBUM_NAME
            mediaFile.AlbumArtist = ARTIST_NAME
            mediaFile.SaveMetadata()

        coll = MediaCollection(albumPath)
        analysis = CollectionAnalysisAlbumDirectoryNamingConvention()
        result = analysis.RunAnalysis(coll)
        
        self.assertEqual(result.AnalysisType, AnalysisType.CollectionAlbumDirectoryNamingConvention)
        self.assertFalse(result.HasIssues)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()