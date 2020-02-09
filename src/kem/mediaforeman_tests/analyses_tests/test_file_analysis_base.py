import unittest
import shutil
from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.media_collection import MediaCollection
from kem.mediaforeman_tests.test_asset_constants import TestAssetConstants
from kem.mediaforeman.analyses.file_analysis_media_file_type import FileAnalysisMediaFileType
from kem.mediaforeman.analyses.file_analysis_valid_image import FileAnalysisValidImage
from kem.mediaforeman.analyses.analysis_type import AnalysisType

class TestFileAnalysisBase(TestBaseFs):

    def test_file_analysis_against_collection_runs_once_for_each_file(self):
        artistDir = self.CreateSubDirectory(dirName='test_artist')
        albumDir = self.CreateSubDirectory(dirName="test_album", dirPath=artistDir)
        
        self.CopySampleMp3ToDir(testDir = albumDir, testFile = TestAssetConstants.SAMPLE_MP3_NO_METADATA)
        
        '''copy 2 mp3 files and rename them to .asdf'''
        '''this will trigger 2 issues in the result from the analysis'''
        for i in range(0, 2):
            notaMP3 = self.CopySampleMp3ToDir(testDir = albumDir, testFile = TestAssetConstants.SAMPLE_MP3_NO_METADATA)
            shutil.copy(notaMP3, "{}.asdf".format(notaMP3))
        
        mediaColl = MediaCollection(artistDir)
        analysis = FileAnalysisMediaFileType()
        results = analysis.RunAnalysis(mediaColl)
        
        self.assertTrue(results.HasIssues)
        self.assertEqual(len(results.IssuesFound), 2)
        
    def test_file_analysis_against_collection_multiple_issues_on_2_files_reports_all_in_results(self):
        artistDir = self.CreateSubDirectory(dirName='test_artist')
        albumDir = self.CreateSubDirectory(dirName="test_album", dirPath=artistDir)
        
        self.CopySampleMp3ToDir(testDir = albumDir, testFile = TestAssetConstants.SAMPLE_MP3_MEETS_SIZE_REQS)
        
        sample1 = self.CopySampleMp3ToDir(testDir = albumDir, testFile = TestAssetConstants.SAMPLE_MP3_NO_METADATA)
        sample2 = self.CopySampleMp3ToDir(testDir = albumDir, testFile = TestAssetConstants.SAMPLE_MP3_NO_METADATA)
        
        mediaColl = MediaCollection(artistDir)
        analysis = FileAnalysisValidImage()
        results = analysis.RunAnalysis(mediaColl)
        
        self.assertTrue(results.HasIssues)
        self.assertEqual(len(results.IssuesFound), 6)
        self.assertEqual(len([file for file in results.IssuesFound if file.MediaFile.BasePath == sample1]), 3)
        self.assertEqual(len([file for file in results.IssuesFound if file.MediaFile.BasePath == sample2]), 3)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()