from mediaforeman.analyses.file_analysis_base import FileAnalysisBase
from mediaforeman.analyses.analysis_type import AnalysisType
from mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from mediaforeman.analyses.analysis_issue_type import AnalysisIssuePropertyType
import os
from mediaforeman.analyses.analysis_fix_single_property import AnalysisFixSingleProperty
from test.test_sys_settrace import arigo_example0
from mutagen import trueaudio
from mediaforeman.analyses.analysis_fix_error import AnalysisFixError

class FileAnalysisTrackNamingConvention(FileAnalysisBase):

    def __init__(self):
        pass
        
    def GetAnalysisType(self):
        return AnalysisType.FileTrackNamingConvention

    def RunAnalysisOnFile(self, mediaFile):
        results = []
        
        expectedName = self.GetExpectedName(mediaFile)
        actualName = mediaFile.GetNameNoExtension()
        
        if(expectedName != actualName):
            results.append(AnalysisIssuePropertyInvalid(
                mediaFile, 
                AnalysisIssuePropertyType.TrackNamingConvention, 
                expectedName, 
                actualName
            ))
            
        return results
    
    def AreAllExpectedNamePropertiesValid(self, mediaFile):
        if(mediaFile.TrackNumber >= 0 and mediaFile.Title != "" and mediaFile.Album != ""):
            return True
        
        return False
    
    def GetExpectedName(self, mediaFile):
        return "{0:02d} - {1} - {2}".format(
            mediaFile.TrackNumber,
            mediaFile.Title,
            mediaFile.Album 
        )

    def FixIssues(self, media):
        
        if(self.AreAllExpectedNamePropertiesValid(media) == False):
            return [AnalysisFixError(media, self.GetAnalysisType())]
        
        fix = AnalysisFixSingleProperty(media, self.GetAnalysisType())

        correctedName = self.GetExpectedName(media)
        correctedPath = os.path.join(media.GetParentDirPath(), correctedName + media.GetFileExtension())
        
        os.rename(media.BasePath, correctedPath)

        '''update the files path'''
        fix.ChangeFrom = media.BasePath
        media.BasePath = correctedPath
        fix.ChangeTo = correctedPath

        return [fix]
        