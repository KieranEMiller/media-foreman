import unittest
from mediaforeman_tests.test_base_fs import TestBaseFs
from mediaforeman.media_file import MediaFile
from mediaforeman.media_collection import MediaCollection
from mediaforeman.analyses.analysis_type import AnalysisType
from mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from mediaforeman.analyses.collection_analysis_same_album_in_directory import CollectionAnalysisSameAlbumInDirectory

class TestCollectionAnalysisSameAlbumInDirectory(TestBaseFs):

    def create_file_system_sample_mp3_with_album_name(self, dir = None, name = ""):
        path = self.CopySampleMp3ToDir(testDir = dir)
        sample = MediaFile(path)
        sample.Album = name
        sample.SaveMetadata()
        return path

    def test_analysis_flat_dir_structure_all_same_artist(self):
        rootTestDir = self.CreateSubDirectory("tmp")
        self.create_file_system_sample_mp3_with_album_name(rootTestDir, "artist2")
        self.create_file_system_sample_mp3_with_album_name(rootTestDir, "artist2")
        self.create_file_system_sample_mp3_with_album_name(rootTestDir, "artist2")
        self.create_file_system_sample_mp3_with_album_name(rootTestDir, "artist2")

        coll = MediaCollection(rootTestDir)
        analysis = CollectionAnalysisSameAlbumInDirectory()
        result = analysis.RunAnalysis(coll)
        
        self.assertEqual(result.AnalysisType, AnalysisType.CollectionSameAlbumInDirectory)
        self.assertFalse(result.HasIssues)

    def test_analysis_flat_dir_structure_different_artists(self):
        rootTestDir = self.CreateSubDirectory("tmp")
        self.create_file_system_sample_mp3_with_album_name(rootTestDir, "artist1")
        self.create_file_system_sample_mp3_with_album_name(rootTestDir, "artist2")
        self.create_file_system_sample_mp3_with_album_name(rootTestDir, "artist2")
        self.create_file_system_sample_mp3_with_album_name(rootTestDir, "artist2")
        self.create_file_system_sample_mp3_with_album_name(rootTestDir, "artist1")
        
        coll = MediaCollection(rootTestDir)
        analysis = CollectionAnalysisSameAlbumInDirectory()
        result = analysis.RunAnalysis(coll)
        
        self.assertEqual(result.AnalysisType, AnalysisType.CollectionSameAlbumInDirectory)
        self.assertTrue(result.HasIssues)
        self.assertEqual(len(result.IssuesFound), 2)
        
        for issue in result.IssuesFound:
            self.assertIsInstance(issue, AnalysisIssuePropertyInvalid)
            self.assertEqual(issue.ActualVal, "artist1")
            
    def test_analysis_flat_dir_structure_different_artists_same_counts_picks_one(self):
        rootTestDir = self.CreateSubDirectory("tmp")
        self.create_file_system_sample_mp3_with_album_name(rootTestDir, "artist1")
        self.create_file_system_sample_mp3_with_album_name(rootTestDir, "artist2")
        self.create_file_system_sample_mp3_with_album_name(rootTestDir, "artist2")
        self.create_file_system_sample_mp3_with_album_name(rootTestDir, "artist1")
        
        coll = MediaCollection(rootTestDir)
        analysis = CollectionAnalysisSameAlbumInDirectory()
        result = analysis.RunAnalysis(coll)
        
        self.assertEqual(result.AnalysisType, AnalysisType.CollectionSameAlbumInDirectory)
        self.assertTrue(result.HasIssues)
        self.assertEqual(len(result.IssuesFound), 2)
        
        for issue in result.IssuesFound:
            self.assertIsInstance(issue, AnalysisIssuePropertyInvalid)
            self.assertEqual(issue.ActualVal, "artist2")

    def test_analysis_complex_dir_structure_different_artists_but_all_in_same_dir(self):
        rootTestDir = self.CreateSubDirectory("tmp")
        self.create_file_system_sample_mp3_with_album_name(rootTestDir, "artist2")
        
        subdir1_1 = self.CreateSubDirectory("sub11", dirPath=rootTestDir)
        self.create_file_system_sample_mp3_with_album_name(subdir1_1, "artist3")
        self.create_file_system_sample_mp3_with_album_name(subdir1_1, "artist3")
        
        subsubdir = self.CreateSubDirectory("subsubdir", dirPath=subdir1_1)
        self.create_file_system_sample_mp3_with_album_name(subsubdir, "artist1")
        self.create_file_system_sample_mp3_with_album_name(subsubdir, "artist1")
        self.create_file_system_sample_mp3_with_album_name(subsubdir, "artist1")

        coll = MediaCollection(rootTestDir)
        analysis = CollectionAnalysisSameAlbumInDirectory()
        result = analysis.RunAnalysis(coll)
        
        self.assertEqual(result.AnalysisType, AnalysisType.CollectionSameAlbumInDirectory)
        self.assertFalse(result.HasIssues)
        
    def test_analysis_complex_dir_one_dir_diff_artists(self):
        rootTestDir = self.CreateSubDirectory("tmp")
        self.create_file_system_sample_mp3_with_album_name(rootTestDir, "artist2")
        self.create_file_system_sample_mp3_with_album_name(rootTestDir, "artist2")
        self.create_file_system_sample_mp3_with_album_name(rootTestDir, "artist2")
        
        subdir1_1 = self.CreateSubDirectory("sub11", dirPath=rootTestDir)
        self.create_file_system_sample_mp3_with_album_name(subdir1_1, "artist3")
        self.create_file_system_sample_mp3_with_album_name(subdir1_1, "artist3")
        self.create_file_system_sample_mp3_with_album_name(subdir1_1, "artist1")
        
        coll = MediaCollection(rootTestDir)
        analysis = CollectionAnalysisSameAlbumInDirectory()
        result = analysis.RunAnalysis(coll)
        
        self.assertEqual(result.AnalysisType, AnalysisType.CollectionSameAlbumInDirectory)
        self.assertTrue(result.HasIssues)
        self.assertEqual(len(result.IssuesFound), 1)
        
        for issue in result.IssuesFound:
            self.assertIsInstance(issue, AnalysisIssuePropertyInvalid)
            self.assertEqual(issue.ActualVal, "artist1")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()