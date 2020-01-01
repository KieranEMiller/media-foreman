'''
Created on Dec 29, 2019

@author: kieranemiller
'''
import unittest
import shutil
import tempfile
import os

class TestBaseFs(unittest.TestCase):

    def setUp(self):
        self._testDir = tempfile.mkdtemp()
        return self._testDir

    def tearDown(self):
        shutil.rmtree(self._testDir)

    def CreateSubDirectory(self, name):
        newDir = os.path.join(self._testDir, name)
        os.mkdir(newDir)
        return newDir
    
    def CopySampleMp3ToDir(self, dir):
        pathToSample = "./assets/sample_mp3.mp3"
        dest = os.path.join(self._testDir, os.path.basename(pathToSample));
        shutil.copy(os.path.abspath(pathToSample), dest)
        return dest
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()