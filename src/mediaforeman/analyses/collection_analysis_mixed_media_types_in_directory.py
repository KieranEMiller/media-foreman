import logging
from mediaforeman.analyses.collection_analysis_base import CollectionAnalysisBase
from mediaforeman.analyses.analysis_type import AnalysisType
from mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from mediaforeman.util.most_common_determinator import MostCommonDeterminator
from mediaforeman.analyses.analysis_issue_type import AnalysisIssuePropertyType
from mediaforeman.util.media_related_file_type_detector import MediaRelatedFileTypeDetector

_log = logging.getLogger()

class CollectionAnalysisMixedMediaTypesInDirectory(CollectionAnalysisBase):

    def __init__(self):
        pass
    
    def GetAnalysisType(self):
        return AnalysisType.CollectionMixedMediaTypesInDirectory
        
    def RunAnalysisOnCollection(self, mediaColl):
        determinator = MostCommonDeterminator()
        mostCommonExt = determinator.ComputeMostCommonItemInList([file.GetFileExtension() for file in mediaColl.MediaFiles])
        
        relatedMedia = MediaRelatedFileTypeDetector()
        results = []
        for media in mediaColl.MediaFiles:
            '''do not consider files that are of a related media type, like .cue or .log'''
            if(relatedMedia.IsExtensionOnPathAMatch(media.BasePath)):
                continue
            
            if(media.GetFileExtension() != mostCommonExt):
                results.append(AnalysisIssuePropertyInvalid(
                    media, AnalysisIssuePropertyType.MixedFileType, mostCommonExt, media.GetFileExtension()
                ))

        return results