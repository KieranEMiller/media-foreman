from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.analyses.file_analysis_media_file_type import FileAnalysisMediaFileType
from kem.mediaforeman.analyses.file_analysis_complete_audio_metadata import FileAnalysisCompleteAudioMetadata
from kem.mediaforeman.analyses.file_analysis_minimum_quality_standards import FileAnalysisMinimumQualityStandards
from kem.mediaforeman.analyses.file_analysis_valid_image import FileAnalysisValidImage
from kem.mediaforeman.analyses.collection_analysis_mixed_media_types_in_directory import CollectionAnalysisMixedMediaTypesInDirectory
from kem.mediaforeman.analyses.collection_analysis_same_album_in_directory import CollectionAnalysisSameAlbumInDirectory
from kem.mediaforeman.analyses.collection_analysis_same_artist import CollectionAnalysisSameArtist
class AnalysisTypeFactory(object):

    def __init__(self):
        pass
        
    def TypeToAnalysis(self, type):
        switcher = {
            AnalysisType.FileMediaType: FileAnalysisMediaFileType,
            AnalysisType.FileCompleteAudioMetadata: FileAnalysisCompleteAudioMetadata,
            AnalysisType.FileMinimumQualityStandards: FileAnalysisMinimumQualityStandards,
            AnalysisType.FileValidImage: FileAnalysisValidImage,
            
            AnalysisType.CollectionMixedMediaTypesInDirectory: CollectionAnalysisMixedMediaTypesInDirectory,
            AnalysisType.CollectionSameAlbumInDirectory: CollectionAnalysisSameAlbumInDirectory,
            AnalysisType.CollectionSameArtist: CollectionAnalysisSameArtist
        }
        return switcher[type]