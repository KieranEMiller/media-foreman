'''
Created on Dec 29, 2019

@author: kieranemiller
'''
import unittest
import shutil
import tempfile
import os
import uuid

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
        pathToSample = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets/sample_mp3.mp3")
        dest = os.path.join(self._testDir, "{}.mp3".format(str(uuid.uuid1())));
        shutil.copy(os.path.abspath(pathToSample), dest)
        '''print("copying sample mp3 from {} to {}".format(os.path.abspath(pathToSample), dest))'''
        return dest
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()