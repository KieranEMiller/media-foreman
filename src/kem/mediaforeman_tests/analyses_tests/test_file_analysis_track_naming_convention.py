import unittest
from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman.media_file import MediaFile
from kem.mediaforeman.analyses.file_analysis_track_naming_convention import FileAnalysisTrackNamingConvention
import shutil

class Test(TestBaseFs):

    def test_track_number_is_padded_to_2_digits(self):
        expectedName = "03 - testAlbum - testArtist.mp3"
        file = "asdf"#self.CopySampleMp3ToDir(destFileName=)

        
        mediaFile = MediaFile(file)
        mediaFile.Album="testAlbum"
        mediaFile.TrackNumber=3
        mediaFile.AlbumArtist="testArtist"
        
        analysis = FileAnalysisTrackNamingConvention()
        result = analysis.RunAnalysis(mediaFile)
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()