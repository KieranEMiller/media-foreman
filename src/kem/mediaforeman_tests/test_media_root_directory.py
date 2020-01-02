'''
Created on Dec 29, 2019

@author: kieranemiller
'''
import unittest
from kem.mediaforeman_tests.test_base_fs import TestBaseFs

from kem.mediaforeman.media_root_directory import MediaRootDirectory
from kem.mediaforeman.media_file import MediaFile
from kem.mediaforeman.media_collection import MediaCollection

class TestMediaRootDirectory(TestBaseFs):

    def test_root_directory_does_not_exist_raises_exception(self):
        mediaroot = MediaRootDirectory(['/some/path/that/doesnt/exist'])
        
        with self.assertRaises(ValueError):
            mediaroot.Process()
            
    def test_empty_root_directory_exists_does_not_raise_exception(self):
        mediaroot = MediaRootDirectory([self._testDir])
        mediaroot.Process()
        self.assertTrue(True)

    def test_single_file_in_root_directory_creates_one_media_file(self):
        self.CopySampleMp3ToDir(self._testDir)
        mediaroot = MediaRootDirectory([self._testDir])
        results = mediaroot.Process()
        self.assertEqual(len(results), 1)
        self.assertIs(type(results[0]), MediaFile)
        
    def test_single_folder_in_root_directory_creates_one_media_collection(self):
        path = self.CreateSubDirectory("test")
        mediaroot = MediaRootDirectory([self._testDir])
        results = mediaroot.Process()
        self.assertEqual(len(results), 1)
        self.assertIs(type(results[0]), MediaCollection)
        
    def test_two_folders_3_files_in_root_directory_creates_multiple_media_types(self):
        dir1 = self.CreateSubDirectory("test1")
        dir2 = self.CreateSubDirectory("test2")

        self.CopySampleMp3ToDir(self._testDir)
        self.CopySampleMp3ToDir(self._testDir)
        self.CopySampleMp3ToDir(self._testDir)

        mediaroot = MediaRootDirectory([self._testDir])
        results = mediaroot.Process()
        self.assertEqual(len(results), 5)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()