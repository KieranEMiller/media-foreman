
class AnalysisResult(object):

    def __init__(self):
        self.ElapsedInMicroSecs = -1
        
        self.AnalysisObj = None
        self.AnalysisType = None
        
        self.Media = None

        self.HasIssues = False
        self.IssuesFound = []