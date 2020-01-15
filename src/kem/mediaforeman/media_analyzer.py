import datetime

from kem.mediaforeman.media_analyzer_result import MediaAnalyzerResult
from kem.mediaforeman.analyses.file_analysis_media_file_type import FileAnalysisMediaFileType
from kem.mediaforeman.analyses.collection_analysis_same_artist import CollectionAnalysisSameArtist

class MediaAnalyzer(object):

    def __init__(self, media, analyses = None):
        self._media = media
        self._analyses = analyses
        
        if(analyses is None):
            self._analyses = [FileAnalysisMediaFileType()]
        
    def Analyze(self, summaryOnly = True):
        
        startTime = datetime.datetime.now()

        result = MediaAnalyzerResult()
        result.AnalysesRun.extend(self._analyses)
        
        '''TODO: decide if its better to iterate over media or by analysis type?'''
        for media in self._media:
            for analysis in self._analyses:
                analysisResults = analysis.RunAnalysis(media = media)
                result.AnalysisResults.append(analysisResults)

        result.ElapsedInMicroSecs = (datetime.datetime.now() - startTime).microseconds
        return result