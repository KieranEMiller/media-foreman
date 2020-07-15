from kem.mediaforeman.analyses.file_analysis_base import FileAnalysisBase
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.analyses.analysis_issue_property_invalid import AnalysisIssuePropertyInvalid
from kem.mediaforeman.analyses.analysis_issue_type import AnalysisIssuePropertyType
import os
from kem.mediaforeman.analyses.analysis_fix_single_property import AnalysisFixSingleProperty

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
    
    def GetExpectedName(self, mediaFile):
        return "{0:02d} - {1} - {2}".format(
            mediaFile.TrackNumber,
            mediaFile.Title,
            mediaFile.Album 
        )

    def FixIssues(self, media):
        fix = AnalysisFixSingleProperty(media, self.GetAnalysisType())
        fix.ChangeFrom = media.BasePath

        correctedName = self.GetExpectedName(media)
        correctedPath = os.path.join(media.GetPath(), correctedName + media.GetFileExtension())
        
        os.rename(media.BasePath, correctedPath)

        '''update the files path'''
        media.BasePath = correctedPath
        
        fix.ChangeTo = correctedPath

        return [fix]
        