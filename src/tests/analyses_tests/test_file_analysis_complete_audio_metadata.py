import unittest
from tests.test_base_fs import TestBaseFs
from mediaforeman.media_file import MediaFile
from mediaforeman.analyses.file_analysis_complete_audio_metadata import FileAnalysisCompleteAudioMetadata
from mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from tests.test_asset_constants import TestAssetConstants
from mediaforeman.analyses.analysis_issue_type import AnalysisIssuePropertyType

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

    def test_null_track_number_does_not_error_out_keeps_default_value(self):
        sample = self.CopySampleMp3ToDir(testFile = TestAssetConstants.SAMPLE_MP3_COMPLETE_METADATA)
        media = MediaFile(sample)
        media.TrackNumber = None
        media.SaveMetadata()

        self.assertIsNone(media.TrackNumber)
        media2 = MediaFile(sample)
        
        analysis = FileAnalysisCompleteAudioMetadata()
        result = analysis.RunAnalysis(media2)
        
        self.assertTrue(result.HasIssues)
        self.assertEqual(len(result.IssuesFound), 1)
        self.assertEqual(result.IssuesFound[0].IssueType, AnalysisIssuePropertyType.TrackNumberInvalid)
        
    def test_fix_issues_raises_error(self):
        sample = self.CopySampleMp3ToDir(testFile = TestAssetConstants.SAMPLE_MP3_NO_METADATA)
        media = MediaFile(sample)
        
        analysis = FileAnalysisCompleteAudioMetadata()
        result = analysis.RunAnalysis(media)
        
        self.assertTrue(result.HasIssues)
        self.assertEqual(len(result.IssuesFound), 4)
        
        self.assertRaises(ValueError, analysis.FixIssues)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()