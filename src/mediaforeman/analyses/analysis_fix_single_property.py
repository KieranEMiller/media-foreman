from mediaforeman.analyses.analysis_fix_base import AnalysisFixBase

class AnalysisFixSingleProperty(AnalysisFixBase):

    def __init__(self, media, analysisType):
        super(AnalysisFixSingleProperty, self).__init__(media, analysisType)        

        self.ChangeFrom = ""
        self.ChangeTo = ""
    
    def GetText(self):
        return "AnalysisFixSingleProperty: {}: for media {}, changed from {} to {}".format(
            self.AnalysisType,
            self.Media.BasePath,
            self.ChangeFrom,
            self.ChangeTo
        )