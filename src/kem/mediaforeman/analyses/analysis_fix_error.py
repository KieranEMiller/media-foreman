from kem.mediaforeman.analyses.analysis_fix_base import AnalysisFixBase

class AnalysisFixError(AnalysisFixBase):

    def __init__(self, media, analysisType):
        super(AnalysisFixError, self).__init__(media, analysisType)        

        self.ErrorMsg = ""
    
    def GetText(self):
        return "AnalysisFixError: {}: for media {}: {}".format(
            self.AnalysisType,
            self.Media.BasePath,
            self.ErrorMsg
        )