import os
from kem.mediaforeman.metadata_parsers.mp3parser import Mp3Parser
from kem.mediaforeman.metadata_parsers.flacparser import FlacParser

class ParserFactory(object):

    def __init__(self, params):
        pass
    
    def GetParserFromFilePath(self, path):
        ext = self.GetFileExtension(path).lower()
        
        if(ext == "mp3"):
            return Mp3Parser(path)
        
        elif(ext == "flac"):
            return FlacParser(path)
        
        raise Exception("unknown file extension for parsing: {}".format(ext))
        
    def GetFileExtension(self, path):
        '''splitext returns a tuple filename, fileext, so index 1 
           is the extension'''
        return os.path.splitext(path)[1]