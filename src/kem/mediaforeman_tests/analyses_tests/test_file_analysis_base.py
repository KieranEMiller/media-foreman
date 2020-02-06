import unittest
from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.media_collection import MediaCollection
from kem.mediaforeman_tests.test_asset_constants import TestAssetConstants
from kem.mediaforeman.analyses.file_analysis_complete_audio_metadata import FileAnalysisCompleteAudioMetadata

class TestFileAnalysisBase(TestBaseFs):

    def test_file_analysis_against_collection_runs_once_for_each_file(self):
        artistDir = self.CreateSubDirectory(dirName='test_artist')
        albumDir = self.CreateSubDirectory(dirName="test_album", dirPath=artistDir)
        
        self.CopySampleMp3ToDir(testDir = albumDir, testFile = TestAssetConstants.SAMPLE_MP3_NO_METADATA)
        self.CopySampleMp3ToDir(testDir = albumDir, testFile = TestAssetConstants.SAMPLE_MP3_NO_METADATA)
        self.CopySampleMp3ToDir(testDir = albumDir, testFile = TestAssetConstants.SAMPLE_MP3_NO_METADATA)
        
        mediaColl = MediaCollection(artistDir)
        analysis = FileAnalysisCompleteAudioMetadata()
        results = analysis.RunAnalysis(mediaColl)
        
        self.assertTrue(results.HasIssues)
        self.assertEqual(len(results.IssuesFound), 12)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()