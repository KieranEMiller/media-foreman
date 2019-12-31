'''
Created on Dec 29, 2019

@author: kieranemiller
'''
import unittest
from kem.mediaforeman_tests.base_fs_tests import BaseFsTests

from kem.mediaforeman.mediaroot import MediaRoot

class TestMediaRoot(TestBaseFs):

    def test_root_directory_does_not_exist_raises_exception(self):
        mediaroot = MediaRoot(['/some/path/that/doesnt/exist'])
        mediaroot.Start()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()