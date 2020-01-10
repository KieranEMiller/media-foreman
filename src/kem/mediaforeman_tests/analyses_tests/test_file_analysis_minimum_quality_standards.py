'''
Created on Jan 8, 2020

@author: KieranM
'''
import unittest
from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.media_file import MediaFile
from kem.mediaforeman.analyses.file_analysis_minimum_quality_standards import FileAnalysisMinimumQualityStandards
from kem.mediaforeman.analyses.analysis_type import AnalysisType

SAMPLE_MP3_172bitrate = "./assets/sample_mp3_172bitrate.mp3"
SAMPLE_MP3_320bitrate = "./assets/sample_mp3_320bitrate.mp3"

class TestFileAnalysisMinimumQualityStandards(TestBaseFs):

    def test_file_with_valid_standards_returns_no_issues(self):
        samplePath = self.CopySampleMp3ToDir(testFile = SAMPLE_MP3_320bitrate)
        mediaFile = MediaFile(samplePath)
        
        analysis = FileAnalysisMinimumQualityStandards()
        result = analysis.RunAnalysis(mediaFile)
        
        self.assertFalse(result.HasIssues)
        self.assertEqual(len(result.IssuesFound), 0)
        self.assertEqual(result.AnalysisType, AnalysisType.FileMinimumQualityStandards)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()