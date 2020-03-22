import unittest
from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.media_collection import MediaCollection

class TestMediaCollection(TestBaseFs):

    def test_sets_base_class_full_path_property(self):
        path = self.CreateSubDirectory("test")
        mediaColl = MediaCollection(path)
        self.assertEqual(mediaColl.BasePath, path)
    
    def test_flat_directory_no_sub_dirs_loads_all_files(self):
        root = self.CreateSubDirectory("tmp")
        
        self.CopySampleMp3ToDir(root)
        self.CopySampleMp3ToDir(root)

        mediaColl = MediaCollection(root)

        self.assertEqual(len(mediaColl.MediaFiles), 2)

    def test_complex_dir_structure_multiple_sub_dirs_loads_all_files(self):
        root = self.CreateSubDirectory("tmp1")
        self.CopySampleMp3ToDir(root)
        
        subdir1 = self.CreateSubDirectory("tmp1-1", root)
        self.CopySampleMp3ToDir(subdir1)
        
        subsubdir1 = self.CreateSubDirectory("tmp1-1-1", subdir1)
        self.CopySampleMp3ToDir(subsubdir1)
        self.CopySampleMp3ToDir(subsubdir1)

        subdir1 = self.CreateSubDirectory("tmp2-1", root)
        self.CopySampleMp3ToDir(subdir1)

        mediaColl = MediaCollection(root)

        self.assertEqual(len(mediaColl.MediaFiles), 5)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()