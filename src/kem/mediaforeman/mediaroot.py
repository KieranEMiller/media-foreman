'''
Created on Dec 29, 2019

@author: kieranemiller
'''
import os

class MediaRoot(object):

    def __init__(self, params):
        self._rootDirs = params
        
        'defaults'
        self.summarize = True
    
    def Start(self):
        print("starting eval of {} directories: {}".format(len(self._rootDirs), self._rootDirs))
        if(self.summarize): 
            print("\tsummarize enabled...analysis only\n")
            
        for dir in self._rootDirs:
            self.ProcessRoot(dir)
            
    def ProcessRoot(self, root):
        artists = os.listdir(root)
        print("processing root dir {}, with {} children".format(root, len(artists)))
        
        