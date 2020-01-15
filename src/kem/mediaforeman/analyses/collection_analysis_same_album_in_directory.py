import logging
from kem.mediaforeman.analyses.collection_analysis_base import CollectionAnalysisBase
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from kem.mediaforeman.media_collection import MediaCollection

_log = logging.getLogger()

class CollectionAnalysisSameAlbumInDirectory(CollectionAnalysisBase):

    def __init__(self):
        pass
    
    def GetAnalysisType(self):
        return AnalysisType.CollectionSameArtist
        
    def RunAnalysisOnCollection(self, mediaColl):
        _log.info("running same album analysis on collection: {} with {} files".format(
            mediaColl.BasePath, len(mediaColl.MediaFiles)
        ))
        
        results = []
        for media in mediaColl.MediaFiles:
            pass

        return results
        
    def GetDistinctParentDirs(self, mediaColl):
        parentDirs = {}
        for file in mediaColl.MediaFiles:
            if(file.ParentDirectory in parentDirs):
                parentDirs[file.ParentDirectory] += 1
            else:
                parentDirs[file.ParentDirectory] = 1
            
        return parentDirs
