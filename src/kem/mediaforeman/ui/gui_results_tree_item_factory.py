from kem.mediaforeman.ui.gui_constants import GUIConstants
from kem.mediaforeman.analyses.analysis_issue_media_skipped import AnalysisIssueMediaSkipped
class GUIResultsTreeItemFactory(object):

    def __init__(self):
        pass
    
    def AddParentToResultsTree(self, tree, analysisType, results):
        
        totalNumIssues = sum(1 for result in results if result.HasIssues == True)
        avgProcessingTime = 0
        if(len(results) > 0):
            avgProcessingTime = sum(result.ElapsedInMicroSecs for result in results) / len(results)

        parentNode = self.AddTreeNode(
            tree = tree,
            parent=None,
            text="{}".format(
                analysisType, 
            ),
            values=(
                "{} items".format(len(results)),
                "avg processing time {} us".format(
                    avgProcessingTime
                ),
                "total # issues {}".format(totalNumIssues)
            ),
            tags = (GUIConstants.RESULTS_TREE_TAG_HAS_ISSUES) if totalNumIssues > 0 else GUIConstants.RESULTS_TREE_TAG_HAS_NOISSUES
        )
        return parentNode
    
    def AddAnalysisToResultsTree(self, tree, analysisResult, parent = ''):
        
        '''the values list used in tree.insert are the following columns '''
        '''
        GUIConstants.RESULTS_TREE_COLUMN_HEADER_FILENAME, 
        GUIConstants.RESULTS_TREE_COLUMN_HEADER_PATH, 
        GUIConstants.RESULTS_TREE_COLUMN_HEADER_PARENT_DIR
        '''
        newNode = self.AddTreeNode(
            tree=tree,
            parent=parent, 
            text="{}".format(
                analysisResult.Media.GetName()
            ),
            values=(
                 analysisResult.Media.GetName(),
                 analysisResult.Media.BasePath,
                 analysisResult.Media.ParentDirectory
            ),
            tags = (self.GetTagListByAnalysisResult(analysisResult))
        )
        
        for issue in analysisResult.IssuesFound:
            
            tags = self.GetTagListByAnalysisResult(analysisResult)
            if(isinstance(issue, AnalysisIssueMediaSkipped)):
                tags = GUIConstants.RESULTS_TREE_TAG_WAS_NOT_PROCESSED

            self.AddTreeNode(
                tree, 
                newNode, 
                text="{}".format(
                    issue.GetText()
                ),
                values=(
                    issue.MediaFile.GetName(),
                    issue.MediaFile.BasePath, 
                    issue.MediaFile.ParentDirectory
                ),
                tags = tags
            )
        
        return newNode
    
    def AddTreeNode(self, tree, parent, text, values, tags):
        newNode = tree.insert(
            parent if parent is not None else '', 
            'end', 
            text=text,
            values=values,
            tags=tags
        )
        return newNode
    
    def GetTagListByAnalysisResult(self, analysisResult):
       
        if(analysisResult.WasProcessed == False):
            return GUIConstants.RESULTS_TREE_TAG_WAS_NOT_PROCESSED
        
        elif (analysisResult.HasIssues):
            return GUIConstants.RESULTS_TREE_TAG_HAS_ISSUES
        
        elif (analysisResult.HasIssues == False):
            return GUIConstants.RESULTS_TREE_TAG_HAS_NOISSUES
            