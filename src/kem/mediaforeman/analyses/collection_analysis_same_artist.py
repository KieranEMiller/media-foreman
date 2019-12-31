'''
Created on Dec 30, 2019

@author: kieranemiller
'''
from kem.mediaforeman.analyses.collection_analysis_base import CollectionAnalysisBase
from kem.mediaforeman.analyses.analysis_type import AnalysisType

class CollectionAnalysisSameArtist(CollectionAnalysisBase):

    def __init__(self, params):
        pass
    
    def GetAnalysisType(self):
        return AnalysisType.CollectionSameArtist
        