import logging
from kem.mediaforeman.analyses.collection_analysis_base import CollectionAnalysisBase
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from kem.mediaforeman.util.most_common_determinator import MostCommonDeterminator
from kem.mediaforeman.analyses.analysis_issue_type import AnalysisIssuePropertyType

_log = logging.getLogger()

class CollectionAnalysisMixedMediaTypesInDirectory(CollectionAnalysisBase):

    def __init__(self):
        pass
    
    def GetAnalysisType(self):
        return AnalysisType.CollectionMixedMediaTypesInDirectory
        
    def RunAnalysisOnCollection(self, mediaColl):
        determinator = MostCommonDeterminator()
        mostCommonExt = determinator.ComputeMostCommonItemInList([file.GetFileExtension() for file in mediaColl.MediaFiles])
        
        results = []
        for media in mediaColl.MediaFiles:
            if(media.GetFileExtension() != mostCommonExt):
                results.append(AnalysisIssuePropertyInvalid(
                    media, AnalysisIssuePropertyType.MixedFileType, mostCommonExt, media.GetFileExtension()
                ))

        return results
       