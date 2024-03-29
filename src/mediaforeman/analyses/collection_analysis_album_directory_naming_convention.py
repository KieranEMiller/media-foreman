import logging
import os

from mediaforeman.analyses.collection_analysis_base import CollectionAnalysisBase
from mediaforeman.analyses.analysis_type import AnalysisType
from mediaforeman.util.most_common_determinator import MostCommonDeterminator
from mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from mediaforeman.analyses.analysis_issue_type import AnalysisIssuePropertyType
from mediaforeman.analyses.analysis_fix_error import AnalysisFixError
from mediaforeman.analyses.analysis_fix_single_property import AnalysisFixSingleProperty

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
    
    def FixIssues(self, media):
        results = []
        
        parents = self.GetDistinctParentDirs(media)
        results = []
        for parent in parents:
            
            determinator = MostCommonDeterminator()
            likelyAlbumName = determinator.ComputeMostCommonItemInList([mediaFile.Album for mediaFile in parents[parent]])
            likelyAlbumArtist = determinator.ComputeMostCommonItemInList([mediaFile.AlbumArtist for mediaFile in parents[parent]])
                
            if(likelyAlbumName == "" or likelyAlbumArtist == ""):
                return [AnalysisFixError(media, self.GetAnalysisType())]
            
            correctedName = self.GetExpectedName(likelyAlbumName, likelyAlbumArtist)
            correctedPath = os.path.join(media.GetParentDirPath(), correctedName)
                     
            fix = AnalysisFixSingleProperty(media, self.GetAnalysisType())

            os.rename(media.BasePath, correctedPath)

            '''update the files path'''
            fix.ChangeFrom = media.BasePath
            media.BasePath = correctedPath
            fix.ChangeTo = correctedPath
            results.append(fix)

        return results
        
    