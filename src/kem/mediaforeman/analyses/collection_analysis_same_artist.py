import logging
from kem.mediaforeman.analyses.collection_analysis_base import CollectionAnalysisBase
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid

_log = logging.getLogger()

class CollectionAnalysisSameArtist(CollectionAnalysisBase):

    def __init__(self):
        pass
    
    def GetAnalysisType(self):
        return AnalysisType.CollectionSameArtist
        
    def RunAnalysisOnCollection(self, mediaColl):
        _log.info("running analysis on collection: {} with {} files".format(
            mediaColl.BasePath, len(mediaColl.MediaFiles)
        ))
        artistName = self.GetMostLikelyArtistName(mediaColl.MediaFiles)
        
        results = []
        for media in mediaColl.MediaFiles:
            if(media.AlbumArtist != artistName):
                results.append(AnalysisIssuePropertyInvalid("ArtistNameInconsistency", artistName, media.AlbumArtist))

        return results
        
    def GetMostLikelyArtistName(self, mediaFiles):
        artistCounts = self.ComputeUniqueArtistNames(mediaFiles)
        topArtistName, artistVal = self.GetHighestCountKeyFromDictionary(artistCounts)

        _log.info("likely artist name: most probable is '{}' with a count of {} from {} unique artists and {} files".format(
                topArtistName, artistCounts[topArtistName], len(artistCounts), len(mediaFiles)
            )
        )
        return topArtistName
        
    def ComputeUniqueArtistNames(self, mediaFiles):
        countsByArtistName = {}
        for mediaFile in mediaFiles:
            if(mediaFile.AlbumArtist in countsByArtistName):
                countsByArtistName[mediaFile.AlbumArtist] += 1
            else:
                countsByArtistName[mediaFile.AlbumArtist] = 1
        
        return countsByArtistName
    
    def GetHighestCountKeyFromDictionary(self, countsByName):
        sortedItems = sorted(countsByName.items(), reverse=True, key=lambda x: x[1])
        return sortedItems[0]