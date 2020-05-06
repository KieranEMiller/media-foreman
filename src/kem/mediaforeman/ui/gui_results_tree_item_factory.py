from kem.mediaforeman.ui.gui_constants import GUIConstants
from kem.mediaforeman.analyses.analysis_issue_media_skipped import AnalysisIssueMediaSkipped
class GUIResultsTreeItemFactory(object):

    def __init__(self):
        pass
    
    def AddParentToResultsTree(self, tree, analysisType, results):
        
        totalNumMediaIssues = sum(1 for result in results if result.HasIssues == True)
        totalNumIssuesForAllMedia = sum(len(result.IssuesFound) for result in results if result.HasIssues == True)
        
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
                "avg processing time {0:.2f} us".format(
                    avgProcessingTime
                ),
                "{} media with issues ({} total issues found) (".format(totalNumMediaIssues, totalNumIssuesForAllMedia)
            ),
            tags = (GUIConstants.RESULTS_TREE_TAG_HAS_ISSUES) if totalNumMediaIssues > 0 else GUIConstants.RESULTS_TREE_TAG_HAS_NOISSUES
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
                tags = self.GetTagListByAnalysisResult(analysisResult)#tags
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
       
        numIssuesSkipped = sum(1 for issue in analysisResult.IssuesFound if isinstance(issue, AnalysisIssueMediaSkipped))
        '''only flag the item as not processed if all the issues were MediaSkipped
            AND there is at least one issue to prevent issues from appearing as skipped 
            they had no issues at all'''
        if(numIssuesSkipped == len(analysisResult.IssuesFound) and len(analysisResult.IssuesFound) > 0):
            return GUIConstants.RESULTS_TREE_TAG_WAS_NOT_PROCESSED

        elif(analysisResult.WasProcessed == False):
            return GUIConstants.RESULTS_TREE_TAG_WAS_NOT_PROCESSED
        
        elif (analysisResult.HasIssues):
            return GUIConstants.RESULTS_TREE_TAG_HAS_ISSUES
        
        elif (analysisResult.HasIssues == False):
            return GUIConstants.RESULTS_TREE_TAG_HAS_NOISSUES
            