import unittest

from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.media_collection import MediaCollection
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.media_file import MediaFile
from kem.mediaforeman.analyses.collection_analysis_album_directory_naming_convention import CollectionAnalysisAlbumDirectoryNamingConvention
from kem.mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from kem.mediaforeman.analyses.analysis_issue_type import AnalysisIssuePropertyType
import os

class TestCollectionAnalysisAlbumDirectoryNamingConvention(TestBaseFs):

    def test_correct_album_dir_name_returns_no_issues(self):
        
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

    def test_correct_album_dir_name_with_files_with_multiple_names_returns_no_issues(self):
        ARTIST_NAME = "ArtistTest"
        ALBUM_NAME="Album01Test"
        
        albumPath = self.CreateSubDirectory(dirName = "{} - {}".format(ARTIST_NAME, ALBUM_NAME))

        '''copy files with the same name'''
        for i in range(0, 4):
            filePath = self.CopySampleMp3ToDir(testDir=albumPath)
            mediaFile = MediaFile(filePath)
            mediaFile.Album = ALBUM_NAME
            mediaFile.AlbumArtist = ARTIST_NAME
            mediaFile.SaveMetadata()

        wrongAlbum = self.CopySampleMp3ToDir(testDir=albumPath)
        wrongAlbum  = MediaFile(filePath)
        wrongAlbum.Album = "qwer"
        wrongAlbum.AlbumArtist = ARTIST_NAME
        wrongAlbum.SaveMetadata()

        wrongArtist = self.CopySampleMp3ToDir(testDir=albumPath)
        wrongArtist  = MediaFile(filePath)
        wrongArtist.Album = ALBUM_NAME
        wrongArtist.AlbumArtist = "asdf"
        wrongArtist.SaveMetadata()
        
        coll = MediaCollection(albumPath)
        analysis = CollectionAnalysisAlbumDirectoryNamingConvention()
        result = analysis.RunAnalysis(coll)
        
        self.assertEqual(result.AnalysisType, AnalysisType.CollectionAlbumDirectoryNamingConvention)
        self.assertFalse(result.HasIssues)

    def test_incorrect_album_portion_of_dir_name_returns_issues(self):
        
        ARTIST_NAME = "ArtistTest"
        ALBUM_NAME="Album01Test"
        
        albumPath = self.CreateSubDirectory(dirName = "{} - {}".format(ARTIST_NAME, ALBUM_NAME))

        for i in range(0, 4):
            filePath = self.CopySampleMp3ToDir(testDir=albumPath)
            mediaFile = MediaFile(filePath)
            mediaFile.Album = "qwer"
            mediaFile.AlbumArtist = ARTIST_NAME
            mediaFile.SaveMetadata()

        coll = MediaCollection(albumPath)
        analysis = CollectionAnalysisAlbumDirectoryNamingConvention()
        result = analysis.RunAnalysis(coll)
        
        self.assertTrue(result.HasIssues)
        self.assertEqual(result.AnalysisType, AnalysisType.CollectionAlbumDirectoryNamingConvention)
        self.assertEqual(len(result.IssuesFound), 1)
        self.assertEqual(result.IssuesFound[0].IssueType, AnalysisIssuePropertyType.AlbumDirectoryNamingConvention)
        self.assertEqual(result.IssuesFound[0].ExpectedVal, "{} - {}".format(ARTIST_NAME, "qwer"))
        self.assertEqual(result.IssuesFound[0].ActualVal, "{} - {}".format(ARTIST_NAME, ALBUM_NAME))
        
    def test_fix_issues_corrects_directory_name(self):
        
        ARTIST_NAME = "ArtistTest"
        ALBUM_NAME="Album01Test"
        
        albumPath = self.CreateSubDirectory(dirName = "{} - {}".format(ARTIST_NAME, ALBUM_NAME))

        for i in range(0, 4):
            filePath = self.CopySampleMp3ToDir(testDir=albumPath)
            mediaFile = MediaFile(filePath)
            mediaFile.Album = "qwer"
            mediaFile.AlbumArtist = ARTIST_NAME
            mediaFile.SaveMetadata()

        coll = MediaCollection(albumPath)
        analysis = CollectionAnalysisAlbumDirectoryNamingConvention()
        result = analysis.RunAnalysis(coll)
        
        self.assertTrue(result.HasIssues)
        self.assertEqual(result.AnalysisType, AnalysisType.CollectionAlbumDirectoryNamingConvention)
        self.assertEqual(len(result.IssuesFound), 1)
        self.assertEqual(result.IssuesFound[0].IssueType, AnalysisIssuePropertyType.AlbumDirectoryNamingConvention)
        self.assertEqual(result.IssuesFound[0].ExpectedVal, "{} - {}".format(ARTIST_NAME, "qwer"))
        self.assertEqual(result.IssuesFound[0].ActualVal, "{} - {}".format(ARTIST_NAME, ALBUM_NAME))
        
        expectedDirName = "{} - {}".format(ARTIST_NAME, "qwer")
        expectedAlbumPath = albumPath.replace("{} - {}".format(ARTIST_NAME, ALBUM_NAME), expectedDirName)
        analysis.FixIssues(coll)
        
        self.assertFalse(os.path.isdir(albumPath))
        self.assertTrue(os.path.isdir(expectedAlbumPath))
        self.assertTrue(os.path.exists(expectedAlbumPath))

        coll = MediaCollection(expectedAlbumPath)
        analysis = CollectionAnalysisAlbumDirectoryNamingConvention()
        result = analysis.RunAnalysis(coll)
        
        self.assertFalse(result.HasIssues)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()