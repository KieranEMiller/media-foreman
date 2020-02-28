'''
Created on Dec 29, 2019

@author: kieranemiller
'''
import unittest
import os
from kem.mediaforeman_tests.test_base_fs import TestBaseFs

from kem.mediaforeman.media_root_directory import MediaRootDirectory
from kem.mediaforeman.media_file import MediaFile
from kem.mediaforeman.media_collection import MediaCollection
from kem.mediaforeman_tests.test_asset_constants import TestAssetConstants
from kem.mediaforeman.media_analyzer import MediaAnalyzer
from kem.mediaforeman.analyses.collection_analysis_album_directory_naming_convention import CollectionAnalysisAlbumDirectoryNamingConvention

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
        
    def test_root_dir_respects_max_number_of_dirs_to_process(self):
        
        for i in range(10):
            dir = self.CreateSubDirectory("test_dir_{}".format(str(i)))
            self.CopySampleMp3ToDir(testDir = dir)
            self.CopySampleMp3ToDir(testDir = dir)
            
        self.assertEqual(len(os.listdir(self._testDir)), 10)
            
        mediaroot = MediaRootDirectory([self._testDir])
        results = mediaroot.Process()
        
        '''only assert this condition if the number of directories to process is
        greater than 0; setting this property to 0 or -1 results in no limit and
        this test is meaningless in those cases'''
        if(MediaRootDirectory.MAX_NUMBER_OF_DIRS_IN_ROOT_TO_PROCESS > 0):
            self.assertEqual(len(results), MediaRootDirectory.MAX_NUMBER_OF_DIRS_IN_ROOT_TO_PROCESS)
            
    def test_non_media_file_in_root_process_correctly(self):
        path = self.CopySampleMp3ToDir(testFile = TestAssetConstants.SAMPLE_IMG, destFileName="qwer.png")
        
        mediaroot = MediaRootDirectory([self._testDir])
        results= mediaroot.Process()
        
        analyzer = MediaAnalyzer(results, [CollectionAnalysisAlbumDirectoryNamingConvention()])
        analyzer.Analyze(True)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()