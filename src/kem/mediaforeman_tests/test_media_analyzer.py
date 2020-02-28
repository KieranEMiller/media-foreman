'''
Created on Jan 1, 2020

@author: kieranemiller
'''
import unittest
from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.media_analyzer import MediaAnalyzer
from kem.mediaforeman.media_file import MediaFile
from kem.mediaforeman.analyses.file_analysis_media_file_type import FileAnalysisMediaFileType
from kem.mediaforeman.analyses.file_analysis_complete_audio_metadata import FileAnalysisCompleteAudioMetadata
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.media_collection import MediaCollection
from kem.mediaforeman.analyses.collection_analysis_album_directory_naming_convention import CollectionAnalysisAlbumDirectoryNamingConvention
from kem.mediaforeman.analyses.collection_analysis_mixed_media_types_in_directory import CollectionAnalysisMixedMediaTypesInDirectory
from kem.mediaforeman_tests.test_asset_constants import TestAssetConstants

class TestMediaAnalyzer(TestBaseFs):

    def test_runs_default_analysis_if_none_specified_single_file(self):
        sampleFile = self.CopySampleMp3ToDir()
        media = MediaFile(sampleFile)

        analyzer = MediaAnalyzer([media])
        results = analyzer.Analyze()
        self.assertIsNotNone(results)
        
        self.assertEqual(len(results.AnalysesRun), 1)
        self.assertEqual(len(results.AnalysisResultsByAnalysisType), 1)
        self.assertIsInstance(results.AnalysesRun[0], FileAnalysisMediaFileType)

    def test_runs_analyses_specified_if_set_in_ctor_single_file(self):
        sampleFile = self.CopySampleMp3ToDir()
        media = MediaFile(sampleFile)
        
        analyzer = MediaAnalyzer([media], [FileAnalysisMediaFileType(), FileAnalysisCompleteAudioMetadata()])
        results = analyzer.Analyze()
        self.assertIsNotNone(results)
        
        self.assertEqual(len(results.AnalysesRun), 2)
        self.assertEqual(len(results.AnalysisResultsByAnalysisType), 2)
        self.assertIsInstance(results.AnalysesRun[0], FileAnalysisMediaFileType)
        self.assertIsInstance(results.AnalysesRun[1], FileAnalysisCompleteAudioMetadata)
    
    def test_runs_multiple_analysis_multiple_files(self):
        sampleFile1 = self.CopySampleMp3ToDir()
        media1 = MediaFile(sampleFile1)

        sampleFile2 = self.CopySampleMp3ToDir()
        media2 = MediaFile(sampleFile2)
        
        analyzer = MediaAnalyzer([media1, media2], [FileAnalysisMediaFileType(), FileAnalysisCompleteAudioMetadata()])
        results = analyzer.Analyze()
        self.assertIsNotNone(results)
        
        self.assertEqual(len(results.AnalysesRun), 2)
        self.assertEqual(len(results.AnalysisResultsByAnalysisType), 2)
        self.assertIsInstance(results.AnalysesRun[0], FileAnalysisMediaFileType)
        self.assertIsInstance(results.AnalysesRun[1], FileAnalysisCompleteAudioMetadata)
        self.assertEqual(len(results.AnalysisResultsByAnalysisType[AnalysisType.FileMediaType]), 2)
        self.assertEqual(len(results.AnalysisResultsByAnalysisType[AnalysisType.FileCompleteAudioMetadata]), 2)
        
    def test_runs_on_single_collection_valid_media_types(self):
        dir = self.CreateSubDirectory("test_collection")
        sampleFile1 = self.CopySampleMp3ToDir(testDir = dir)
        sampleFile2 = self.CopySampleMp3ToDir(testDir = dir)

        mediaColl = MediaCollection(dir)
        analyzer = MediaAnalyzer([mediaColl], [CollectionAnalysisMixedMediaTypesInDirectory()])
        results = analyzer.Analyze()

        '''no exceptions'''
        self.assertTrue(True)
        
    def test_runs_on_single_collection_with_some_invalid_media_types(self):
        dir = self.CreateSubDirectory("test_collection")
        sampleFile1 = self.CopySampleMp3ToDir(testDir = dir)
        sampleFile2 = self.CopySampleMp3ToDir(testDir = dir)
        sampleFile3 = self.CopySampleMp3ToDir(testDir = dir, testFile=TestAssetConstants.SAMPLE_IMG)

        mediaColl = MediaCollection(dir)
        analyzer = MediaAnalyzer([mediaColl], [CollectionAnalysisMixedMediaTypesInDirectory()])
        results = analyzer.Analyze()

        '''no exceptions'''
        self.assertTrue(True)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()