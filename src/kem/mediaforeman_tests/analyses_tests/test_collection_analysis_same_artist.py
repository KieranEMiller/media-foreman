import unittest
from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.analyses.collection_analysis_same_artist import CollectionAnalysisSameArtist
from kem.mediaforeman.media_file import MediaFile
from kem.mediaforeman.media_collection import MediaCollection
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid

class Test(TestBaseFs):

    def create_sample_mp3_with_artist_name(self, name):
        sample = MediaFile(path = None)
        sample.AlbumArtist = name
        return sample

    def create_file_system_sample_mp3_with_artist_name(self, dir = None, artistName = ""):
        path = self.CopySampleMp3ToDir(testDir = dir)
        sample = MediaFile(path)
        sample.AlbumArtist = artistName
        sample.SaveMetadata()
        return path

    def test_get_highest_count_key_basic(self):
        dict = {
            "name1": 0,
            "name3": 2,
            "name2": 1
        }
        
        analysis = CollectionAnalysisSameArtist()
        artistName, artistCount = analysis.GetHighestCountKeyFromDictionary(dict)
        
        self.assertEqual(artistName, "name3")
        self.assertEqual(artistCount, 2)
        
    def test_get_highest_count_key_all_zero_picks_first_entry(self):
        dict = {
            "name1": 0,
            "name3": 0,
            "name2": 0
        }
        
        analysis = CollectionAnalysisSameArtist()
        artistName, artistCount = analysis.GetHighestCountKeyFromDictionary(dict)
        
        self.assertEqual(artistName, "name1")
        self.assertEqual(artistCount, 0)
        
    
    def test_compute_unique_artist_names_mixed_counts_basic(self):
        mediaFiles = [
            self.create_sample_mp3_with_artist_name("artist1"),
            self.create_sample_mp3_with_artist_name("artist2"),
            self.create_sample_mp3_with_artist_name("artist1")
        ]
        
        analysis = CollectionAnalysisSameArtist()
        countsByName = analysis.ComputeUniqueArtistNames(mediaFiles)
        
        self.assertEqual(len(countsByName), 2)
        self.assertEqual(countsByName["artist1"], 2)
        self.assertEqual(countsByName["artist2"], 1)

    def test_compute_unique_artist_names_all_counts_1(self):
        mediaFiles = [
            self.create_sample_mp3_with_artist_name("artist1"),
            self.create_sample_mp3_with_artist_name("artist2"),
            self.create_sample_mp3_with_artist_name("artist3")
        ]
        
        analysis = CollectionAnalysisSameArtist()
        countsByName = analysis.ComputeUniqueArtistNames(mediaFiles)
        
        self.assertEqual(len(countsByName), 3)
        
        for name in countsByName:
            self.assertEqual(countsByName[name], 1)

    def test_get_most_likely_artist_name_all_same_name(self):
        mediaFiles = [
            self.create_sample_mp3_with_artist_name("artist1"),
            self.create_sample_mp3_with_artist_name("artist1"),
            self.create_sample_mp3_with_artist_name("artist1")
        ]
        
        analysis = CollectionAnalysisSameArtist()
        likelyArtist = analysis.GetMostLikelyArtistName(mediaFiles)
        
        self.assertEqual(likelyArtist, "artist1")

    def test_get_most_likely_artist_name_all_distinct_names_returns_first_one(self):
        mediaFiles = [
            self.create_sample_mp3_with_artist_name("artist2"),
            self.create_sample_mp3_with_artist_name("artist1"),
            self.create_sample_mp3_with_artist_name("artist3")
        ]
        
        analysis = CollectionAnalysisSameArtist()
        likelyArtist = analysis.GetMostLikelyArtistName(mediaFiles)
        
        self.assertEqual(likelyArtist, "artist2")

    def test_get_most_likely_artist_name_mixed_counts(self):
        mediaFiles = [
            self.create_sample_mp3_with_artist_name("artist2"),
            self.create_sample_mp3_with_artist_name("artist1"),
            self.create_sample_mp3_with_artist_name("artist2"),
            self.create_sample_mp3_with_artist_name("artist3"),
            self.create_sample_mp3_with_artist_name("artist1"),
            self.create_sample_mp3_with_artist_name("artist1")
        ]
        
        analysis = CollectionAnalysisSameArtist()
        likelyArtist = analysis.GetMostLikelyArtistName(mediaFiles)
        
        self.assertEqual(likelyArtist, "artist1")
        
    def test_full_analysis_all_same_artist_flat_dir_structure_returns_no_issues(self):
        rootTestDir = self.CreateSubDirectory("tmp")
        self.create_file_system_sample_mp3_with_artist_name(rootTestDir, "artist1")
        self.create_file_system_sample_mp3_with_artist_name(rootTestDir, "artist2")
        self.create_file_system_sample_mp3_with_artist_name(rootTestDir, "artist2")
        self.create_file_system_sample_mp3_with_artist_name(rootTestDir, "artist2")
        self.create_file_system_sample_mp3_with_artist_name(rootTestDir, "artist1")
        
        coll = MediaCollection(rootTestDir)
        analysis = CollectionAnalysisSameArtist()
        result = analysis.RunAnalysis(coll)
        
        self.assertEqual(result.AnalysisType, AnalysisType.CollectionSameArtist)
        self.assertTrue(result.HasIssues)
        self.assertEqual(len(result.IssuesFound), 2)
        
        for issue in result.IssuesFound:
            self.assertIsInstance(issue, AnalysisIssuePropertyInvalid)
            self.assertEqual(issue.ActualVal, "artist1")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()