'''
Created on Dec 31, 2019

@author: kieranemiller
'''
from kem.mediaforeman.analyses.file_analysis_media_file_type import FileAnalysisMediaFileType

class MediaAnalyzer(object):

    def __init__(self, media):
        self._media = media
        
    def Analyze(self, summaryOnly):
        
        fileAnalyses = [FileAnalysisMediaFileType]
        
        for media in self._media:
            print("analyzing media {}".format(media))