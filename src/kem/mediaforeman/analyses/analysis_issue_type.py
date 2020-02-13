'''
Created on Dec 31, 2019

@author: kieranemiller
'''
from enum import Enum

class AnalysisIssuePropertyType(Enum):
    MetadataFieldEmpty = 1
    AlbumMismatch = 2
    ArtistMismatch = 3
    FileType = 4
    LossyClassification = 5
    CoverImageExists = 6
    CoverImageXDimensions = 7
    CoverImageYDimensions = 8
    BitRate = 9
    MixedFileType = 10
    TrackNumberInvalid = 11
