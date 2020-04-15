from kem.mediaforeman.metadata_parsers.base_parser import BaseParser

class Mp3Parser(BaseParser):

    def __init__(self, path):
        super(self, path).__init__(path)
        