import unittest
from kem.mediaforeman.metadata_parsers.flacparser import FlacParser
from kem.mediaforeman_tests.test_base_fs import TestBaseFs
from kem.mediaforeman_tests.test_asset_constants import TestAssetConstants

class FlacParserTests(TestBaseFs):

    def test_load_sample_flac_file(self):
        flacMedia = self.CopySampleMp3ToDir(testFile=TestAssetConstants.SAMPLE_FLAC)
        parser = FlacParser(flacMedia)
        result = parser.ExtractProperties()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()