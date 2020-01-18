import logging
from kem.mediaforeman.analyses.collection_analysis_base import CollectionAnalysisBase
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from kem.mediaforeman.util.most_common_determinator import MostCommonDeterminator

_log = logging.getLogger()

class CollectionAnalysisMixedMediaTypesInDirectory(CollectionAnalysisBase):

    def __init__(self):
        pass
    
    def GetAnalysisType(self):
        return AnalysisType.CollectionSameArtist
        
    def RunAnalysisOnCollection(self, mediaColl):
        _log.info("running mixed media analysis on collection: {} with {} files".format(
            mediaColl.BasePath, len(mediaColl.MediaFiles)
        ))
        
        '''
        determinator = MostCommonDeterminator()
         = determinator.ComputeMostCommonItemInList([file.GetFileName() for file in mediaColl.MediaFiles])
        
        results = []
        for media in mediaColl.MediaFiles:
            if(media.AlbumArtist != artistName):
                results.append(AnalysisIssuePropertyInvalid("ArtistNameInconsistency", artistName, media.AlbumArtist))

        return results
        '''
       