'''
Created on Jan 1, 2020

@author: kieranemiller
'''
import unittest
from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.media_analyzer import MediaAnalyzer
from kem.mediaforeman.media_file import MediaFile

class TestMediaAnalyzer(TestBaseFs):

    def test_media_analyzer_runs_default_analysis_if_none_specified(self):
        sampleFile = self.CopySampleMp3ToDir(self._testDir)
        media = MediaFile(sampleFile)

        analyzer = MediaAnalyzer([media])
        results = analyzer.Analyze()
        self.assertIsNotNone(results)
        
        self.assertGreater(len(results.AnalysesRun), 0)
        self.assertGreater(len(results.AnalysisResults), 0)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()