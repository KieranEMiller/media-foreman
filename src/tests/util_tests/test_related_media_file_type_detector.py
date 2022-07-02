import unittest
from tests.test_base_fs import TestBaseFs
from mediaforeman.util.media_related_file_type_detector import MediaRelatedFileTypeDetector

class TestRelatedMediaFileTypeDetector(TestBaseFs):

    def test_file_with_non_matching_extension_returns_false(self):
        path = self.CopySampleMp3ToDir(destFileName='test.mp3')
        
        relatedMediaDetector = MediaRelatedFileTypeDetector()
        
        self.assertFalse(relatedMediaDetector.IsExtensionOnPathAMatch(path))
    
    def test_file_with_matching_extension_returns_true(self):
        path = self.CopySampleMp3ToDir(destFileName='test.cue')
        
        relatedMediaDetector = MediaRelatedFileTypeDetector()
        
        self.assertTrue(relatedMediaDetector.IsExtensionOnPathAMatch(path))
        
    def test_file_with_matching_extension_returns_true_regardless_of_case(self):
        path = self.CopySampleMp3ToDir(destFileName='test.CuE')
        
        relatedMediaDetector = MediaRelatedFileTypeDetector()
        
        self.assertTrue(relatedMediaDetector.IsExtensionOnPathAMatch(path))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()