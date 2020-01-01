'''
Created on Dec 29, 2019

@author: kieranemiller
'''
import os

from kem.mediaforeman.media_collection import MediaCollection
from kem.mediaforeman.media_file import MediaFile

class MediaRootDirectory(object):

    def __init__(self, params):
        self._rootDirs = params
        
        'defaults'
        self.summarize = True
    
    def Process(self):
        print("starting eval of {} directories: {}".format(len(self._rootDirs), self._rootDirs))
        if(self.summarize): 
            print("\tsummarize enabled...analysis only\n")
            
        media = []
        for dir in self._rootDirs:
            media.extend(self.ProcessRoot(dir))
            
        return media
            
    def ProcessRoot(self, root):
        if(not os.path.isdir(root)):
            raise ValueError("unknown directory {}".format(root))
        
        dirContents = os.listdir(root)
        print("processing root dir {}, with {} children".format(root, len(dirContents)))

        media = []
        for fileOrFolder in dirContents:
            path = os.path.join(root, fileOrFolder)
            if(os.path.isdir(path)):
                media.append(MediaCollection(path))
                
            elif(os.path.isfile(path)):
                media.append(MediaFile(path))
            
        return media
        