import unittest
from tests.test_base_fs import TestBaseFs
from mediaforeman.media_file import MediaFile
from mediaforeman.analyses.file_analysis_minimum_quality_standards import FileAnalysisMinimumQualityStandards
from mediaforeman.analyses.analysis_type import AnalysisType
from mediaforeman.analyses.analysis_issue_threshold_not_met import AnalysisIssueThresholdNotMet
from tests.test_asset_constants import TestAssetConstants

class TestFileAnalysisMinimumQualityStandards(TestBaseFs):

    def test_file_with_valid_standards_returns_no_issues(self):
        samplePath = self.CopySampleMp3ToDir(testFile = TestAssetConstants.SAMPLE_MP3_320bitrate)
        mediaFile = MediaFile(samplePath)
        
        analysis = FileAnalysisMinimumQualityStandards()
        result = analysis.RunAnalysis(mediaFile)
        
        self.assertFalse(result.HasIssues)
        self.assertEqual(len(result.IssuesFound), 0)
        self.assertEqual(result.AnalysisType, AnalysisType.FileMinimumQualityStandards)

    def test_file_with_invalid_standards_returns_issues(self):
        sample = self.CopySampleMp3ToDir(testFile = TestAssetConstants.SAMPLE_MP3_172bitrate)
        mediaFile = MediaFile(sample)
        
        analysis = FileAnalysisMinimumQualityStandards()
        result = analysis.RunAnalysis(mediaFile)
        
        self.assertTrue(result.HasIssues)
        self.assertGreater(len(result.IssuesFound), 0)
        self.assertIsInstance(result.IssuesFound[0], AnalysisIssueThresholdNotMet)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()