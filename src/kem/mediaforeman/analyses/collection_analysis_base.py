'''
Created on Dec 30, 2019

@author: kieranemiller
'''
from abc import abstractmethod

from kem.mediaforeman.analyses.analysis_base import AnalysisBase

class CollectionAnalysisBase(AnalysisBase):

    def __init__(self, params):
        pass
    
    @abstractmethod
    def RunAnalysisOnCollection(self, mediaColl):
        pass
    
        