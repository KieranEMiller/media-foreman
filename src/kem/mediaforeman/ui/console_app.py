'''
Created on Dec 29, 2019

@author: kieranemiller
'''
import argparse
import logging

from kem.mediaforeman.media_root_directory import MediaRootDirectory
from kem.mediaforeman.media_analyzer import MediaAnalyzer
from kem.mediaforeman.app_config import AppConfig

_log = logging.getLogger()

class ConsoleApp(object):

    def __init__(self):
        self._args = None
        self._args = self.ParseArgs()
        
        config = AppConfig()
        self._config = config.GetFromCommandLineArguments(self._args)
        
    def Run(self):
        _log.info("processing root directory {}".format(self._config.RootDirectories))

        processor = MediaRootDirectory(self._config.RootDirectories)
        media = processor.Process()
        
        analyzer = MediaAnalyzer(media, self._config.AnalysesToRun)
        summary = analyzer.Analyze(self._config.SummarizeOnly)
        
    def ParseArgs(self):
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

        argParser.add_argument("-a", 
                               "--analyze", 
                               help="specify the analyses to run", 
                               action="append",
                               required=False)
        
        return argParser.parse_args()
        
