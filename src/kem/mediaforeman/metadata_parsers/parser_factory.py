import os
from kem.mediaforeman.metadata_parsers.mp3parser import Mp3Parser
from kem.mediaforeman.metadata_parsers.flacparser import FlacParser
import logging

_log = logging.getLogger()

class ParserFactory(object):

    def __init__(self):
        pass
    
    def GetParserFromFilePath(self, path):
        ext = self.GetFileExtension(path).lower()
        
        if(ext == ".mp3"):
            return Mp3Parser(path)
        
        elif(ext == ".flac"):
            return FlacParser(path)
        
        _log.warn("unable to load media type parser: unknown file extension '{}'".format(ext))
        return None
        
    def GetFileExtension(self, path):
        '''splitext returns a tuple filename, fileext, so index 1 
           is the extension'''
        return os.path.splitext(path)[1]