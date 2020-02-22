'''
Created on Dec 31, 2019

@author: kieranemiller
'''
from enum import Enum

class AnalysisType(Enum):
    FileMediaType = 1
    FileValidImage = 2
    FileCompleteAudioMetadata = 3
    FileMinimumQualityStandards = 4
    FileTrackNamingConvention = 9
    
    CollectionSameArtist = 5
    CollectionSameAlbumInDirectory = 6
    CollectionMixedMediaTypesInDirectory = 7
    CollectionAlbumDirectoryNamingConvention = 8