import unittest
from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.media_collection import MediaCollection
from kem.mediaforeman.media_file import MediaFile

class Test(TestBaseFs):

    def test_parent_directory_set_for_media_collection(self):
        dirPath = self.CreateSubDirectory("tmp1")
        
        expectedParent = self._testDir
        coll = MediaCollection(dirPath)
        
        self.assertEqual(coll.ParentDirectory, expectedParent)

    def test_parent_directory_set_for_media_file(self):
        filePath = self.CopySampleMp3ToDir()

        expectedParent = self._testDir
        mediaFile = MediaFile(filePath)
        
        self.assertEqual(mediaFile.ParentDirectory, expectedParent)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()