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
        
        parents = self.GetDistinctParentDirs(mediaColl)
        results = []
        for parent in parents:
            
            
            

        return results
        
    def GetDistinctParentDirs(self, mediaColl):
        parentDirs = {}
        for file in mediaColl.MediaFiles:
            if(file.ParentDirectory in parentDirs):
                parentDirs[file.ParentDirectory].append(file)
            else:
                parentDirs[file.ParentDirectory] = [file]
            
        return parentDirs
