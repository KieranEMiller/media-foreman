'''
Created on Jan 1, 2020

@author: kieranemiller
'''

class AnalysisResult(object):

    def __init__(self):
        self.ElapsedInMicroSecs = -1
        self.AnalysisType = None
        self.Media = None

        self.HasIssues = False
        self.IssuesFound = []