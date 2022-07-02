import unittest
from mediaforeman.util.most_common_determinator import MostCommonDeterminator
from mediaforeman.media_file import MediaFile

class TestMostCommonDeterminator(unittest.TestCase):
    
    def create_sample_mp3_with_artist_name(self, name):
        sample = MediaFile(path = None)
        sample.AlbumArtist = name
        return sample
    
    def test_get_highest_count_key_basic(self):
        dict = {
            "name1": 0,
            "name3": 2,
            "name2": 1
        }
        
        determinator = MostCommonDeterminator()
        artistName, artistCount = determinator.GetHighestCountKeyFromDictionary(dict)
        
        self.assertEqual(artistName, "name3")
        self.assertEqual(artistCount, 2)
        
    def test_get_highest_count_key_all_zero_picks_first_entry(self):
        dict = {
            "name1": 0,
            "name3": 0,
            "name2": 0
        }
        
        determinator = MostCommonDeterminator()
        artistName, artistCount = determinator.GetHighestCountKeyFromDictionary(dict)
        
        self.assertEqual(artistName, "name1")
        self.assertEqual(artistCount, 0)
        
    
    def test_compute_unique_artist_names_mixed_counts_basic(self):
        mediaFiles = [
            self.create_sample_mp3_with_artist_name("artist1"),
            self.create_sample_mp3_with_artist_name("artist2"),
            self.create_sample_mp3_with_artist_name("artist1")
        ]
        
        determinator = MostCommonDeterminator()
        countsByName = determinator.CountUnique([file.AlbumArtist for file in mediaFiles])
        
        self.assertEqual(len(countsByName), 2)
        self.assertEqual(countsByName["artist1"], 2)
        self.assertEqual(countsByName["artist2"], 1)

    def test_compute_unique_artist_names_all_counts_1(self):
        mediaFiles = [
            self.create_sample_mp3_with_artist_name("artist1"),
            self.create_sample_mp3_with_artist_name("artist2"),
            self.create_sample_mp3_with_artist_name("artist3")
        ]
        
        determinator = MostCommonDeterminator()
        countsByName = determinator.CountUnique([file.AlbumArtist for file in mediaFiles])
        
        self.assertEqual(len(countsByName), 3)
        
        for name in countsByName:
            self.assertEqual(countsByName[name], 1)

    def test_get_most_likely_artist_name_all_same_name(self):
        mediaFiles = [
            self.create_sample_mp3_with_artist_name("artist1"),
            self.create_sample_mp3_with_artist_name("artist1"),
            self.create_sample_mp3_with_artist_name("artist1")
        ]
        
        determinator = MostCommonDeterminator()
        likelyArtist = determinator.ComputeMostCommonItemInList([file.AlbumArtist for file in mediaFiles])
        
        self.assertEqual(likelyArtist, "artist1")

    def test_get_most_likely_artist_name_all_distinct_names_returns_first_one(self):
        mediaFiles = [
            self.create_sample_mp3_with_artist_name("artist2"),
            self.create_sample_mp3_with_artist_name("artist1"),
            self.create_sample_mp3_with_artist_name("artist3")
        ]
        
        determinator = MostCommonDeterminator()
        likelyArtist = determinator.ComputeMostCommonItemInList([file.AlbumArtist for file in mediaFiles])
        
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
        
        determinator = MostCommonDeterminator()
        likelyArtist = determinator.ComputeMostCommonItemInList([file.AlbumArtist for file in mediaFiles])
        
        self.assertEqual(likelyArtist, "artist1")
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()