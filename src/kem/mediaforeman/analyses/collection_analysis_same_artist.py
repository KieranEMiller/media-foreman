import logging
from kem.mediaforeman.analyses.collection_analysis_base import CollectionAnalysisBase
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from kem.mediaforeman.util.most_common_determinator import MostCommonDeterminator

_log = logging.getLogger()

class CollectionAnalysisSameArtist(CollectionAnalysisBase):

    def __init__(self):
        pass
    
    def GetAnalysisType(self):
        return AnalysisType.CollectionSameArtist
        
    def RunAnalysisOnCollection(self, mediaColl):
        _log.info("running same artist analysis on collection: {} with {} files".format(
            mediaColl.BasePath, len(mediaColl.MediaFiles)
        ))
        
        determinator = MostCommonDeterminator()
        artistName = determinator.ComputeMostCommonItemInList([file.AlbumArtist for file in mediaColl.MediaFiles])
        
        results = []
        for media in mediaColl.MediaFiles:
            if(media.AlbumArtist != artistName):
                results.append(AnalysisIssuePropertyInvalid("ArtistNameInconsistency", artistName, media.AlbumArtist))

        return results
       