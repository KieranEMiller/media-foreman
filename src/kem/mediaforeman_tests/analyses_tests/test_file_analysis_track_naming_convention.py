import unittest
from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.media_file import MediaFile
from kem.mediaforeman.analyses.file_analysis_track_naming_convention import FileAnalysisTrackNamingConvention
from kem.mediaforeman.analyses.analysis_issue_type import AnalysisIssuePropertyType

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
        
        analysis.FixIssues(mediaFile)
        
        mediaFile = MediaFile(mediaFile.BasePath)
        result = analysis.RunAnalysis(mediaFile)
        
        self.assertFalse(result.HasIssues)

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()