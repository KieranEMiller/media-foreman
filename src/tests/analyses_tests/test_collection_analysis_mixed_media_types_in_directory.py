import unittest
from tests.test_base_fs import TestBaseFs
from mediaforeman.media_file import MediaFile
from mediaforeman.media_collection import MediaCollection
from mediaforeman.analyses.analysis_type import AnalysisType
from mediaforeman.analyses.collection_analysis_mixed_media_types_in_directory import CollectionAnalysisMixedMediaTypesInDirectory
import shutil
from mediaforeman.analyses.analysis_issue_type import AnalysisIssuePropertyType

class TestCollectionAnalysisMixedMediaTypesInDirectory(TestBaseFs):

    def test_analysis_all_same_types(self):
        self.CopySampleMp3ToDir()
        self.CopySampleMp3ToDir()
        self.CopySampleMp3ToDir()

        coll = MediaCollection(self._testDir)
        analysis = CollectionAnalysisMixedMediaTypesInDirectory()
        result = analysis.RunAnalysis(coll)
        
        self.assertEqual(result.AnalysisType, AnalysisType.CollectionMixedMediaTypesInDirectory)
        self.assertFalse(result.HasIssues)
        
    def test_analysis_mixed_types_marks_least_common_wrong(self):
        self.CopySampleMp3ToDir()
        self.CopySampleMp3ToDir()

        path = self.CopySampleMp3ToDir()
        wrongExtFilePath = "{}.asdf".format(path)
        shutil.copy(path, wrongExtFilePath)

        coll = MediaCollection(self._testDir)
        analysis = CollectionAnalysisMixedMediaTypesInDirectory()
        result = analysis.RunAnalysis(coll)
        
        self.assertEqual(result.AnalysisType, AnalysisType.CollectionMixedMediaTypesInDirectory)
        self.assertTrue(result.HasIssues)
        self.assertEqual(len(result.IssuesFound), 1)
        self.assertEqual(result.IssuesFound[0].IssueType, AnalysisIssuePropertyType.MixedFileType)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()