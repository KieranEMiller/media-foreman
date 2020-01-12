'''
Created on Dec 29, 2019

@author: kieranemiller
'''
import argparse
import logging

from kem.mediaforeman.media_root_directory import MediaRootDirectory
from kem.mediaforeman.media_analyzer import MediaAnalyzer

_log = logging.getLogger()

class ConsoleApp(object):

    def __init__(self, params=None):
        self._args = None
        self.SetupArgs()
        
    def Run(self):
        _log.info("ConsoleApp: processing root directory {}".format(self._args.root_directory))
        processor = MediaRootDirectory(self._args.root_directory)
        
        if(self._args.summary): 
            processor.summarize = True
            
        media = processor.Process()
        
        analyzer = MediaAnalyzer(media)
        summary = analyzer.Analyze(processor.summarize)
        
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
        
        argParser.add_argument("-g",
                               "--gui",
                               help="use the GUI version of the app instead of the console version",
                               required=False,
                               action="store_true")
        
        self._args = argParser.parse_args()
        
