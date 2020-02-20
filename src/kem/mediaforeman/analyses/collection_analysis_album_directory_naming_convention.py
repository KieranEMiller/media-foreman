import logging
import os

from kem.mediaforeman.analyses.collection_analysis_base import CollectionAnalysisBase
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.util.most_common_determinator import MostCommonDeterminator
from kem.mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from kem.mediaforeman.analyses.analysis_issue_type import AnalysisIssuePropertyType

_log = logging.getLogger()

class CollectionAnalysisAlbumDirectoryNamingConvention(CollectionAnalysisBase):

    def __init__(self):
        pass
        
    def GetAnalysisType(self):
        return AnalysisType.CollectionAlbumDirectoryNamingConvention
    
    def GetExpectedName(self, album, artist):
        expectedName = "{} - {}".format(artist, album)
        return expectedName
        
    def RunAnalysisOnCollection(self, mediaColl):
        '''assume parent directories are the album...not ideal'''
        parents = self.GetDistinctParentDirs(mediaColl)
        results = []
        for parent in parents:
            
            _log.info("processing parent {} with {} children".format(
                parent, len(parents[parent])
            ))
            
            determinator = MostCommonDeterminator()
            likelyAlbumName = determinator.ComputeMostCommonItemInList([mediaFile.Album for mediaFile in parents[parent]])
            likelyAlbumArtist = determinator.ComputeMostCommonItemInList([mediaFile.AlbumArtist for mediaFile in parents[parent]])
            
            expectedName = self.GetExpectedName(likelyAlbumName, likelyAlbumArtist)
            
            actualName = os.path.basename(parent)
            if(actualName != expectedName):
                results.append(AnalysisIssuePropertyInvalid(
                    mediaColl, 
                    AnalysisIssuePropertyType.AlbumDirectoryNamingConvention, 
                    expectedName, 
                    actualName
                ))
            
        return results
        
    