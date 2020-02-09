class GUIResultsTreeItemFactory(object):

    def __init__(self):
        pass
    
    def AddParentToResultsTree(self, tree, analysisType, results):
        parentNode = self.AddTreeNode(
            tree = tree,
            parent=None,
            text="{} ({} items in average of {} us)".format(
                analysisType, 
                len(results),
                sum(result.ElapsedInMicroSecs for result in results) / len(results)
            ),
            values=("", "", "")
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
            text="{} - {}".format(
                analysisResult.AnalysisType,
                analysisResult.Media.GetName()
            ),
            values=(
                 analysisResult.Media.GetName(),
                 analysisResult.Media.BasePath,
                 analysisResult.Media.ParentDirectory
            )
        )
        
        for issue in analysisResult.IssuesFound:
            self.AddTreeNode(
                tree, 
                newNode, 
                text="{} - {}".format(
                    issue.IssueType,
                    issue.MediaFile.GetName()
                ),
                values=(
                    issue.MediaFile.GetName(),
                    issue.MediaFile.BasePath, 
                    issue.MediaFile.ParentDirectory
                )
            )
        
        return newNode
    
    def AddTreeNode(self, tree, parent, text, values):
        newNode = tree.insert(
            parent if parent is not None else '', 
            'end', 
            text=text,
            values=values
        )
        return newNode
    