'''
Created on Dec 31, 2019

@author: kieranemiller
'''
from enum import Enum

class AnalysisType(Enum):
    FileMediaType = 1
    FileValidImage = 2
    FileCompleteAudioMetadata = 3
    CollectionSameArtist = 4
        