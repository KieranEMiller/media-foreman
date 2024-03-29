import logging
from mediaforeman.analyses.collection_analysis_base import CollectionAnalysisBase
from mediaforeman.analyses.analysis_type import AnalysisType
from mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from mediaforeman.util.most_common_determinator import MostCommonDeterminator
from mediaforeman.analyses.analysis_issue_type import AnalysisIssuePropertyType

_log = logging.getLogger()

class CollectionAnalysisSameArtist(CollectionAnalysisBase):

    def __init__(self):
        pass
    
    def GetAnalysisType(self):
        return AnalysisType.CollectionSameArtist
        
    def RunAnalysisOnCollection(self, mediaColl):
        determinator = MostCommonDeterminator()
        artistName = determinator.ComputeMostCommonItemInList([file.AlbumArtist for file in mediaColl.MediaFiles])
        
        results = []
        for media in mediaColl.MediaFiles:
            if(media.AlbumArtist != artistName):
                results.append(AnalysisIssuePropertyInvalid(
                    media, AnalysisIssuePropertyType.ArtistMismatch, artistName, media.AlbumArtist
                ))

        return results
       