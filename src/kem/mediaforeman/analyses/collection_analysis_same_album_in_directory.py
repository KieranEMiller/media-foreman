import logging
from kem.mediaforeman.analyses.collection_analysis_base import CollectionAnalysisBase
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from kem.mediaforeman.media_collection import MediaCollection
from kem.mediaforeman.util.most_common_determinator import MostCommonDeterminator
from kem.mediaforeman.analyses.analysis_issue_type import AnalysisIssuePropertyType

_log = logging.getLogger()

class CollectionAnalysisSameAlbumInDirectory(CollectionAnalysisBase):

    def __init__(self):
        pass
    
    def GetAnalysisType(self):
        return AnalysisType.CollectionSameAlbumInDirectory
        
    def RunAnalysisOnCollection(self, mediaColl):
        parents = self.GetDistinctParentDirs(mediaColl)
        results = []
        for parent in parents:
            
            _log.info("processing parent {} with {} children".format(
                parent, len(parents[parent])
            ))
            
            determinator = MostCommonDeterminator()
            likelyAlbumName = determinator.ComputeMostCommonItemInList([mediaFile.Album for mediaFile in parents[parent]])
            
            for mediaFile in parents[parent]:
                if(mediaFile.Album != likelyAlbumName):
                    results.append(AnalysisIssuePropertyInvalid(
                        mediaFile, AnalysisIssuePropertyType.AlbumMismatch, likelyAlbumName, mediaFile.Album
                    ))
            
        return results
        
    def GetDistinctParentDirs(self, mediaColl):
        parentDirs = {}
        for file in mediaColl.MediaFiles:
            if(file.ParentDirectory in parentDirs):
                parentDirs[file.ParentDirectory].append(file)
            else:
                parentDirs[file.ParentDirectory] = [file]
            
        return parentDirs
