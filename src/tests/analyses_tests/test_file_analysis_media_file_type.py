import unittest
import shutil

from tests.test_base_fs import TestBaseFs
from mediaforeman.media_file import MediaFile
from mediaforeman.analyses.file_analysis_media_file_type import FileAnalysisMediaFileType
from mediaforeman.analyses.analysis_type import AnalysisType
from mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid

class TestFileAnalysisMediaFileType(TestBaseFs):

    def test_mp3_file_is_media_type_returns_no_issue(self):
        sample = self.CopySampleMp3ToDir()
        media = MediaFile(sample)
        
        analysis = FileAnalysisMediaFileType()
        result = analysis.RunAnalysis(media)
        
        self.assertFalse(result.HasIssues)
        self.assertEqual(result.AnalysisType, AnalysisType.FileMediaType)

    def test_non_mp3_file_returns_issue(self):
        sample = self.CopySampleMp3ToDir()
        dest = sample.replace(".mp3", ".txt")
        shutil.copyfile(sample, dest)
        
        media = MediaFile(dest)

        analysis = FileAnalysisMediaFileType()
        result = analysis.RunAnalysis(media)
        
        self.assertTrue(result.HasIssues)
        self.assertGreater(len(result.IssuesFound), 0)
        self.assertIsInstance(result.IssuesFound[0], AnalysisIssuePropertyInvalid)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()