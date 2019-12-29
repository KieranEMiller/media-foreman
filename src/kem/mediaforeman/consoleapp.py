'''
Created on Dec 29, 2019

@author: kieranemiller
'''
import argparse

class ConsoleApp(object):

    def __init__(self, params=None):
        self._args = None
        self.SetupArgs()
        
    def Run(self):

        
        if(self._args.omg):
            self.ShowHelp()
        
    def SetupArgs(self):
        argParser = argparse.ArgumentParser("options")

        argParser.add_argument("-d", 
                               "--root-directory", 
                               help="specify the target directory", 
                               action="append",
                               required=True)
        
        self._args = argParser.parse_args()
        
    def ShowHelp(self):
        print("help menu")