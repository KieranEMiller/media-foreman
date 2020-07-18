import unittest
from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.media_file import MediaFile
from kem.mediaforeman.analyses.file_analysis_track_naming_convention import FileAnalysisTrackNamingConvention
from kem.mediaforeman.analyses.analysis_issue_type import AnalysisIssuePropertyType
from kem.mediaforeman.analyses.analysis_fix_error import AnalysisFixError
from kem.mediaforeman.analyses.analysis_fix_single_property import AnalysisFixSingleProperty
import os

class TestFileAnalysisTrackingNamingConvention(TestBaseFs):

    def test_file_name_matching_convention_returns_no_issues(self):
        file = self.CopySampleMp3ToDir(destFileName="03 - testTitle - testAlbum.mp3")

        mediaFile = MediaFile(file)
        mediaFile.Album="testAlbum"
        mediaFile.Title="testTitle"
        mediaFile.TrackNumber=3
        mediaFile.AlbumArtist="testArtist"
        
        analysis = FileAnalysisTrackNamingConvention()
        result = analysis.RunAnalysis(mediaFile)
        
        self.assertFalse(result.HasIssues)
        
    def test_file_name_non_2_digit_track_number_returns_issue(self):
        file = self.CopySampleMp3ToDir(destFileName="3 - testTitle - testAlbum.mp3")

        mediaFile = MediaFile(file)
        mediaFile.Album="testAlbum"
        mediaFile.Title="testTitle"
        mediaFile.TrackNumber=3
        mediaFile.AlbumArtist="testArtist"
        
        analysis = FileAnalysisTrackNamingConvention()
        result = analysis.RunAnalysis(mediaFile)
        
        self.assertTrue(result.HasIssues)
        self.assertTrue(len(result.IssuesFound), 1)
        self.assertEqual(result.IssuesFound[0].IssueType, AnalysisIssuePropertyType.TrackNamingConvention)
        self.assertEqual(result.IssuesFound[0].ExpectedVal, "03 - testTitle - testAlbum")

    def test_file_name_wrong_case_on_title_returns_issue(self):
        file = self.CopySampleMp3ToDir(destFileName="3 - TESTTitle - testAlbum.mp3")

        mediaFile = MediaFile(file)
        mediaFile.Album="testAlbum"
        mediaFile.Title="testTitle"
        mediaFile.TrackNumber=3
        mediaFile.AlbumArtist="testArtist"
        
        analysis = FileAnalysisTrackNamingConvention()
        result = analysis.RunAnalysis(mediaFile)
        
        self.assertTrue(result.HasIssues)
        self.assertTrue(len(result.IssuesFound), 1)
        self.assertEqual(result.IssuesFound[0].IssueType, AnalysisIssuePropertyType.TrackNamingConvention)
        self.assertEqual(result.IssuesFound[0].ExpectedVal, "03 - testTitle - testAlbum")       

    def test_fix_issue_correctly_changes_filename(self):
        file = self.CopySampleMp3ToDir(destFileName="3 - TESTTitle - testAlbum.mp3")

        mediaFile = MediaFile(file)
        mediaFile.Album="testAlbum"
        mediaFile.Title="testTitle"
        mediaFile.TrackNumber=3
        mediaFile.AlbumArtist="testArtist"
        mediaFile.SaveMetadata()
        
        analysis = FileAnalysisTrackNamingConvention()
        result = analysis.RunAnalysis(mediaFile)
        
        self.assertTrue(result.HasIssues)
        self.assertTrue(len(result.IssuesFound), 1)
        self.assertEqual(result.IssuesFound[0].IssueType, AnalysisIssuePropertyType.TrackNamingConvention)
        self.assertEqual(result.IssuesFound[0].ExpectedVal, "03 - testTitle - testAlbum")       
        
        fixes = analysis.FixIssues(mediaFile)
        self.assertEqual(len(fixes), 1)
        self.assertIsInstance(fixes[0], AnalysisFixSingleProperty)
        self.assertEqual(fixes[0].ChangeFrom, file)
        self.assertEqual(fixes[0].ChangeTo, mediaFile.BasePath)
        
        mediaFile = MediaFile(mediaFile.BasePath)
        result = analysis.RunAnalysis(mediaFile)
        
        self.assertFalse(result.HasIssues)
        
    def test_fix_issue_returns_fix_error_when_one_or_more_metadata_fields_not_set(self):
        file = self.CopySampleMp3ToDir(destFileName="3 - TESTTitle - testAlbum.mp3")

        mediaFile = MediaFile(file)
        mediaFile.Album="testAlbum"
        mediaFile.Title=""
        mediaFile.TrackNumber=3
        mediaFile.AlbumArtist="testArtist"
        mediaFile.SaveMetadata()
        
        analysis = FileAnalysisTrackNamingConvention()
        result = analysis.RunAnalysis(mediaFile)
        
        self.assertTrue(result.HasIssues)
        self.assertTrue(len(result.IssuesFound), 1)
        self.assertEqual(result.IssuesFound[0].IssueType, AnalysisIssuePropertyType.TrackNamingConvention)
        self.assertEqual(result.IssuesFound[0].ExpectedVal, "03 -  - testAlbum")       
        
        fixes = analysis.FixIssues(mediaFile)
        self.assertEqual(len(fixes), 1)
        self.assertIsInstance(fixes[0], AnalysisFixError)
        
        self.assertTrue(os.path.isfile(file))

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()