from abc import abstractmethod
import logging

from kem.mediaforeman.analyses.analysis_base import AnalysisBase

_log = logging.getLogger()

class CollectionAnalysisBase(AnalysisBase):

    def __init__(self, params):
        pass
    
    @abstractmethod
    def GetAnalysisType(self):
        pass

    @abstractmethod
    def RunAnalysisOnCollection(self, mediaColl):
        pass
        
    '''
    @abstractmethod
    def ShouldRun(self, media):
        return False
    '''
    
    def IsCollectionAnalysis(self):
        return True
    
    def IsFileAnalysis(self):
        return False
        
    def RunAnalysisOnFile(self, mediaFile):
        msg = "collection analyses do not run against individual files: {}".format(mediaFile.BasePath)
        _log.warn(msg)
        raise ValueError(msg)
    
    def GetDistinctParentDirs(self, mediaColl):
        parentDirs = {}
        for file in mediaColl.MediaFiles:
            if(file.ParentDirectory in parentDirs):
                parentDirs[file.ParentDirectory].append(file)
            else:
                parentDirs[file.ParentDirectory] = [file]
            
        return parentDirs