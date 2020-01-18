import unittest
from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.analyses.collection_analysis_same_artist import CollectionAnalysisSameArtist
from kem.mediaforeman.media_file import MediaFile
from kem.mediaforeman.media_collection import MediaCollection
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid

class Test(TestBaseFs):

    def create_file_system_sample_mp3_with_artist_name(self, dir = None, artistName = ""):
        path = self.CopySampleMp3ToDir(testDir = dir)
        sample = MediaFile(path)
        sample.AlbumArtist = artistName
        sample.SaveMetadata()
        return path

    def test_analysis_flat_dir_structure_all_same_artist(self):
        rootTestDir = self.CreateSubDirectory("tmp")
        self.create_file_system_sample_mp3_with_artist_name(rootTestDir, "artist2")
        self.create_file_system_sample_mp3_with_artist_name(rootTestDir, "artist2")
        self.create_file_system_sample_mp3_with_artist_name(rootTestDir, "artist2")
        self.create_file_system_sample_mp3_with_artist_name(rootTestDir, "artist2")

        coll = MediaCollection(rootTestDir)
        analysis = CollectionAnalysisSameArtist()
        result = analysis.RunAnalysis(coll)
        
        self.assertEqual(result.AnalysisType, AnalysisType.CollectionSameArtist)
        self.assertFalse(result.HasIssues)

    def test_analysis_complex_dir_structure_all_same_artist(self):
        rootTestDir = self.CreateSubDirectory("tmp")
        self.create_file_system_sample_mp3_with_artist_name(rootTestDir, "artist2")
        
        subdir1_1 = self.CreateSubDirectory("sub11", dirPath=rootTestDir)
        self.create_file_system_sample_mp3_with_artist_name(subdir1_1, "artist2")
        self.create_file_system_sample_mp3_with_artist_name(subdir1_1, "artist2")
        
        subsubdir = self.CreateSubDirectory("subsubdir", dirPath=subdir1_1)
        self.create_file_system_sample_mp3_with_artist_name(subsubdir, "artist2")
        
        subdir1_2 = self.CreateSubDirectory("sub12", dirPath=rootTestDir)
        self.create_file_system_sample_mp3_with_artist_name(subdir1_2, "artist2")

        coll = MediaCollection(rootTestDir)
        analysis = CollectionAnalysisSameArtist()
        result = analysis.RunAnalysis(coll)
        
        self.assertEqual(result.AnalysisType, AnalysisType.CollectionSameArtist)
        self.assertFalse(result.HasIssues)

    def test_analysis_flat_dir_structure(self):
        rootTestDir = self.CreateSubDirectory("tmp")
        self.create_file_system_sample_mp3_with_artist_name(rootTestDir, "artist1")
        self.create_file_system_sample_mp3_with_artist_name(rootTestDir, "artist2")
        self.create_file_system_sample_mp3_with_artist_name(rootTestDir, "artist2")
        self.create_file_system_sample_mp3_with_artist_name(rootTestDir, "artist2")
        self.create_file_system_sample_mp3_with_artist_name(rootTestDir, "artist1")
        
        coll = MediaCollection(rootTestDir)
        analysis = CollectionAnalysisSameArtist()
        result = analysis.RunAnalysis(coll)
        
        self.assertEqual(result.AnalysisType, AnalysisType.CollectionSameArtist)
        self.assertTrue(result.HasIssues)
        self.assertEqual(len(result.IssuesFound), 2)
        
        for issue in result.IssuesFound:
            self.assertIsInstance(issue, AnalysisIssuePropertyInvalid)
            self.assertEqual(issue.ActualVal, "artist1")
            
    def test_analysis_complex_dir_structure(self):
        rootTestDir = self.CreateSubDirectory("tmp")
        self.create_file_system_sample_mp3_with_artist_name(rootTestDir, "artist2")
        
        subdir1_1 = self.CreateSubDirectory("sub11", dirPath=rootTestDir)
        self.create_file_system_sample_mp3_with_artist_name(subdir1_1, "artist2")
        self.create_file_system_sample_mp3_with_artist_name(subdir1_1, "artist2")
        
        subsubdir = self.CreateSubDirectory("subsubdir", dirPath=subdir1_1)
        self.create_file_system_sample_mp3_with_artist_name(subsubdir, "artist2")
        self.create_file_system_sample_mp3_with_artist_name(subsubdir, "artist1")
        self.create_file_system_sample_mp3_with_artist_name(subsubdir, "artist2")
        
        subdir1_2 = self.CreateSubDirectory("sub12", dirPath=rootTestDir)
        self.create_file_system_sample_mp3_with_artist_name(subdir1_2, "artist2")

        coll = MediaCollection(rootTestDir)
        analysis = CollectionAnalysisSameArtist()
        result = analysis.RunAnalysis(coll)
        
        self.assertEqual(result.AnalysisType, AnalysisType.CollectionSameArtist)
        self.assertTrue(result.HasIssues)
        self.assertEqual(len(result.IssuesFound), 1)
        
        for issue in result.IssuesFound:
            self.assertIsInstance(issue, AnalysisIssuePropertyInvalid)
            self.assertEqual(issue.ActualVal, "artist1")
            
            
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()