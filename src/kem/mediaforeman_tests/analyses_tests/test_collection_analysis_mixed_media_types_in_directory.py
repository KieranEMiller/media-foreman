import unittest
from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.media_file import MediaFile
from kem.mediaforeman.media_collection import MediaCollection
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.analyses.collection_analysis_mixed_media_types_in_directory import CollectionAnalysisMixedMediaTypesInDirectory
import shutil
from kem.mediaforeman.analyses.analysis_issue_type import AnalysisIssuePropertyType

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