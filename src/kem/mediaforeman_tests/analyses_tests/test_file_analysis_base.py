import unittest
from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.analyses.file_analysis_media_file_type import FileAnalysisMediaFileType
from kem.mediaforeman.media_collection import MediaCollection

class TestFileAnalysisBase(TestBaseFs):

    def test_file_analysis_against_collection_runs_once_for_each_file(self):
        artistDir = self.CreateSubDirectory(dirName='test_artist')
        albumDir = self.CreateSubDirectory(dirName="test_album", dirPath=artistDir)
        
        self.CopySampleMp3ToDir(testDir = albumDir)
        self.CopySampleMp3ToDir(testDir = albumDir)
        self.CopySampleMp3ToDir(testDir = albumDir)
        
        mediaColl = MediaCollection(artistDir)
        analysis = FileAnalysisMediaFileType()
        results = analysis.RunAnalysis(mediaColl)
        
        self.assertTrue(results.HasIssues)
        self.assertEqual(len(results.IssuesFound), 3)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()