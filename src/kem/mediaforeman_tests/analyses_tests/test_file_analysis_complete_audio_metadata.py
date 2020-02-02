import unittest
from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.media_file import MediaFile
from kem.mediaforeman.analyses.file_analysis_complete_audio_metadata import FileAnalysisCompleteAudioMetadata
from kem.mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from kem.mediaforeman_tests.test_asset_constants import TestAssetConstants

class Test(TestBaseFs):

    def test_sample_with_all_metadata_returns_no_issues_sets_defaults(self):
        sample = self.CopySampleMp3ToDir(testFile = TestAssetConstants.SAMPLE_MP3_COMPLETE_METADATA)
        media = MediaFile(sample)
        
        analysis = FileAnalysisCompleteAudioMetadata()
        result = analysis.RunAnalysis(media)

        self.assertFalse(result.HasIssues)
        self.assertEqual(len(result.IssuesFound), 0)
        
    def test_sample_with_no_metadata_returns_issues_sets_defaults(self):
        sample = self.CopySampleMp3ToDir(testFile = TestAssetConstants.SAMPLE_MP3_NO_METADATA)
        media = MediaFile(sample)
        
        analysis = FileAnalysisCompleteAudioMetadata()
        result = analysis.RunAnalysis(media)
        
        self.assertTrue(result.HasIssues)
        self.assertEqual(len(result.IssuesFound), 4)
        
        for issue in result.IssuesFound:
            self.assertIsInstance(issue, AnalysisIssuePropertyInvalid)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()