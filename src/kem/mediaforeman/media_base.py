import os

class MediaBase(object):

    def __init__(self, path):
        self.BasePath = path
        
        if(path != None and os.path.exists(path)):
            self.ParentDirectory = os.path.abspath(os.path.join(path, os.pardir))