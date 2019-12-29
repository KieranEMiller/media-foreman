'''
Created on Dec 29, 2019

@author: kieranemiller
'''
import unittest
import shutil
import tempfile

class BaseFsTests(unittest.TestCase):

    def setUp(self):
        self.testdir = tempfile.mkdtemp()
        print("BaseFsTests: created temp dir {}".format(self.testdir))

    def tearDown(self):
        shutil.rmtree(self.testdir)
        print("BaseFsTests: cleaned temp dir {}".format(self.testdir))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()