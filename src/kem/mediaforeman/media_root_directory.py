'''
Created on Dec 29, 2019

@author: kieranemiller
'''
import os
import logging

from kem.mediaforeman.media_collection import MediaCollection
from kem.mediaforeman.media_file import MediaFile

_log = logging.getLogger()

class MediaRootDirectory(object):
    '''use 0 or -1 to be unlimited'''
    MAX_NUMBER_OF_DIRS_IN_ROOT_TO_PROCESS = 25

    def __init__(self, rootDirs):
        self._rootDirs = rootDirs
        
        'defaults'
        self.summarize = True
    
    def Process(self):
        _log.info("starting eval of {} directories: {}".format(len(self._rootDirs), self._rootDirs))
        if(self.summarize): 
            _log.info("\tsummarize enabled...analysis only\n")
            
        media = []
        for dir in self._rootDirs:
            media.extend(self.ProcessRoot(dir))
            
        return media
            
    def ProcessRoot(self, root):
        if(not os.path.isdir(root)):
            raise ValueError("unknown directory {}".format(root))
        
        dirContents = os.listdir(root)
        _log.info("processing root dir {}, with {} children".format(root, len(dirContents)))

        media = []
        dirsProcessed = 0
        for fileOrFolder in dirContents:
            
            if(self.MAX_NUMBER_OF_DIRS_IN_ROOT_TO_PROCESS > 0 and dirsProcessed >= self.MAX_NUMBER_OF_DIRS_IN_ROOT_TO_PROCESS):
                break
            
            path = os.path.join(root, fileOrFolder)
            if(os.path.isdir(path)):
                media.append(MediaCollection(path))
                dirsProcessed=dirsProcessed+1
                
            elif(os.path.isfile(path)):
                media.append(MediaFile(path))
            
        return media
        