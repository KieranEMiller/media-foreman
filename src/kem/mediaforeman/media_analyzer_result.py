'''
Created on Jan 1, 2020

@author: kieranemiller
'''
from kem.mediaforeman.analyses.analysis_type import AnalysisType

class MediaAnalyzerResult(object):

    def __init__(self):
        self.ElapsedTimeInMicroSec = -1
        self.AnalysesRun = []
        self.AnalysisResultsByAnalysisType = {}
        