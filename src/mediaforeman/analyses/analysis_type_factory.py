from mediaforeman.analyses.analysis_type import AnalysisType
from mediaforeman.analyses.file_analysis_media_file_type import FileAnalysisMediaFileType
from mediaforeman.analyses.file_analysis_complete_audio_metadata import FileAnalysisCompleteAudioMetadata
from mediaforeman.analyses.file_analysis_minimum_quality_standards import FileAnalysisMinimumQualityStandards
from mediaforeman.analyses.file_analysis_valid_image import FileAnalysisValidImage
from mediaforeman.analyses.collection_analysis_mixed_media_types_in_directory import CollectionAnalysisMixedMediaTypesInDirectory
from mediaforeman.analyses.collection_analysis_same_album_in_directory import CollectionAnalysisSameAlbumInDirectory
from mediaforeman.analyses.collection_analysis_same_artist import CollectionAnalysisSameArtist
from mediaforeman.analyses.collection_analysis_album_directory_naming_convention import CollectionAnalysisAlbumDirectoryNamingConvention
from mediaforeman.analyses.file_analysis_track_naming_convention import FileAnalysisTrackNamingConvention

class AnalysisTypeFactory(object):

    def __init__(self):
        pass
        
    def TypeToAnalysis(self, analysisType):
        switcher = {
            AnalysisType.FileMediaType:                 FileAnalysisMediaFileType,
            AnalysisType.FileCompleteAudioMetadata:     FileAnalysisCompleteAudioMetadata,
            AnalysisType.FileMinimumQualityStandards:   FileAnalysisMinimumQualityStandards,
            AnalysisType.FileValidImage:                FileAnalysisValidImage,
            AnalysisType.FileTrackNamingConvention:     FileAnalysisTrackNamingConvention,
            
            AnalysisType.CollectionMixedMediaTypesInDirectory:      CollectionAnalysisMixedMediaTypesInDirectory,
            AnalysisType.CollectionSameAlbumInDirectory:            CollectionAnalysisSameAlbumInDirectory,
            AnalysisType.CollectionSameArtist:                      CollectionAnalysisSameArtist,
            AnalysisType.CollectionAlbumDirectoryNamingConvention:  CollectionAnalysisAlbumDirectoryNamingConvention
        }
        return switcher[analysisType]