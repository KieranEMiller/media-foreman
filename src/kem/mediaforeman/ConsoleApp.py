'''
Created on Dec 29, 2019

@author: kieranemiller
'''
import argparse
from kem.mediaforeman.mediaroot import MediaRoot

class ConsoleApp(object):

    def __init__(self, params=None):
        self._args = None
        self.SetupArgs()
        
    def Run(self):
        processor = MediaRoot(self._args.root_directory)
        
        if(self._args.summary): 
            processor.summarize = True
            
        processor.Start()
        
    def SetupArgs(self):
        argParser = argparse.ArgumentParser("options")

        argParser.add_argument("-d", 
                               "--root-directory", 
                               help="specify the target directory or directories", 
                               action="append",
                               required=True)
        
        argParser.add_argument("-s",
                               "--summary",
                               help="parse the root directory and display statistics.  take no action",
                               required=False,
                               action="store_true")
        
        self._args = argParser.parse_args()
        
