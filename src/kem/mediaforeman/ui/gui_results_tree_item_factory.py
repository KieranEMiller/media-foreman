class GUIResultsTreeItemFactory(object):

    def __init__(self):
        pass
    
    def AddParentToResultsTree(self, tree, analysisType, results):
        parentNode = tree.insert(
            '', 
            'end', 
            text="{} ({} items in average of {} us)".format(
                analysisType, 
                len(results),
                sum(result.ElapsedInMicroSecs for result in results) / len(results)
            ),
            values=(
                "", "", ""
            )
        )
        return parentNode
    
    def AddAnalysisToResultsTree(self, tree, analysisResult, parent = ''):
        
        #parentNode = tree.insert('', 'end', text='item num ' + str(i), values=('qwer', 'qwer', 'qwer'))
        #tree.insert(parentNode, 'end', text='item num ' + str(z), values=('qwer', 'qwer', 'qwer'))
        
        '''the values list used in tree.insert are the following columns '''
        '''
        GUIConstants.RESULTS_TREE_COLUMN_HEADER_FILENAME, 
        GUIConstants.RESULTS_TREE_COLUMN_HEADER_PATH, 
        GUIConstants.RESULTS_TREE_COLUMN_HEADER_PARENT_DIR
        '''
        newNode = tree.insert(
            parent, 
            'end', 
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
        
        return newNode