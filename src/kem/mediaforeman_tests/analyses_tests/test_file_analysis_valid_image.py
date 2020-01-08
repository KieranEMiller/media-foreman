import unittest
from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.analyses.file_analysis_valid_image import FileAnalysisValidImage
from kem.mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from kem.mediaforeman.media_file import MediaFile
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.analyses.analysis_issue_threshold_not_met import AnalysisIssueThresholdNotMet

class TestFileAnalysisValidImage(TestBaseFs):

    def test_returns_no_issues_when_all_properties_met(self):
        samplePath = self.CopySampleMp3WithImgToDir(useSampleWithMinImgReqs=True)
        media = MediaFile(samplePath)
        imgAnalysis = FileAnalysisValidImage(media)
        
        self.assertTrue(media.CoverImgExists)
        
        result = imgAnalysis.RunAnalysis(media)
        self.assertFalse(result.HasIssues)
        self.assertEqual(len(result.IssuesFound), 0)
        
    def test_returns_threshold_not_met_when_size_of_coverart_does_not_meet_min(self):
        samplePath = self.CopySampleMp3WithImgToDir()
        media = MediaFile(samplePath)
        imgAnalysis = FileAnalysisValidImage(media)
        
        self.assertTrue(media.CoverImgExists)
        
        result = imgAnalysis.RunAnalysis(media)
        self.assertTrue(result.HasIssues)
        self.assertGreater(len(result.IssuesFound), 0)
        self.assertIsInstance(result.IssuesFound[0], AnalysisIssueThresholdNotMet)
        self.assertTrue(result.IssuesFound[0].GetText().strip() != "")
        
    def test_returns_property_invalid_issue_when_no_image(self):
        samplePath = self.CopySampleMp3ToDir()
        media = MediaFile(samplePath)
        imgAnalysis = FileAnalysisValidImage(media)
        
        self.assertFalse(media.CoverImgExists)
        
        result = imgAnalysis.RunAnalysis(media)
        self.assertTrue(result.AnalysisType == AnalysisType.FileValidImage)
        self.assertGreater(result.ElapsedInMicroSecs, -1)
        self.assertTrue(result.HasIssues)
        self.assertGreater(len(result.IssuesFound), 0)
        self.assertIsInstance(result.IssuesFound[0], AnalysisIssuePropertyInvalid)
        self.assertTrue(result.IssuesFound[0].GetText().strip() != "")
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()