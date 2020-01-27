import argparse
import logging

_log = logging.getLogger()

class AppConfig(object):

    def __init__(self):
        '''run these analyses'''
        self.AnalysesToRun = []
        
        '''just analyze the root directories, don't actually do anything'''
        self.SummarizeOnly = True
        
        '''the root directories that contain media files'''
        self.RootDirectories = []
        
    def GetFromCommandLineArguments(self, args):
        self.RootDirectories = args.root_directory
        self.SummarizeOnly = args.summary
        
        self.AnalysesToRun = []
        if(args.analyze != None):
            for analysis in args.analyze:
                self.AnalysesToRun.append(analysis())
        
    def PrintConfig(self):
        msg = "configuration: \n\t-analyses: {}; \n\t-root dirs: {}; \n\t-summarize: {}".format(
            self.AnalysesToRun, self.RootDirectories, self.SummarizeOnly
        )
        _log.info(msg)
        return msg.replace("\n\t", "")
        