'''
Created on Dec 30, 2019

@author: kieranemiller
'''
from abc import abstractmethod

class AnalysisBase(object):

    def __init__(self, params):
        pass
    
    @abstractmethod
    def RunAnalysis(self):
        pass
        