import os

class MediaFileTypeDetector(object):

    '''TODO: expand to include additional types.  just audio types for now'''
    VALID_TYPES = ["mp3", "flac", "wav", "ogg", "mp4"]
    
    def __init__(self):
        pass
        
    def IsMediaFileType(self, path):
        '''splitext returns a tuple filename, fileext, so index 1 
           is the extension'''
        extension = os.path.splitext(path)[1].lower()
        match = [extension for extension in self.VALID_TYPES if path.endswith(extension.lower())]
        
        return len(match) != 0