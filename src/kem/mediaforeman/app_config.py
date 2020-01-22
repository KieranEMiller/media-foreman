import argparse

class AppConfig(object):

    def __init__(self, params):
        '''run these analyses'''
        self.AnalysesToRun = []
        
        '''just analyze the root directories, don't actually do anything'''
        self.SummarizeOnly = True
        
        '''the root directories that contain media files'''
        self.RootDirectories = []
        
    def GetFromCommandLineArguments(self, args):
        self.

        