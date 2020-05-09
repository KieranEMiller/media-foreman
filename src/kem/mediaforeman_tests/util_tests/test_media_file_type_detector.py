import unittest
from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.util.media_file_type_detector import MediaFileTypeDetector

class TestMediaFileTypeDetector(TestBaseFs):

    def test_file_with_non_matching_extension_returns_false(self):
        path = self.CopySampleMp3ToDir(destFileName='test.mp3')
        
        mediaDetector = MediaFileTypeDetector()
        
        self.assertTrue(mediaDetector.IsExtensionOnPathAMatch(path))
    
    def test_file_with_matching_extension_returns_true(self):
        path = self.CopySampleMp3ToDir(destFileName='test.cue')
        
        mediaDetector = MediaFileTypeDetector()
        
        self.assertFalse(mediaDetector.IsExtensionOnPathAMatch(path))
        
    def test_file_with_matching_extension_returns_true_regardless_of_case(self):
        path = self.CopySampleMp3ToDir(destFileName='test.MP3')
        
        mediaDetector = MediaFileTypeDetector()
        
        self.assertTrue(mediaDetector.IsExtensionOnPathAMatch(path))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()