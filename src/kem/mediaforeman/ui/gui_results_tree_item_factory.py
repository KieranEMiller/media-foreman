
class GUIResultsTreeItemFactory(object):


    def __init__(self, params):
        pass
    
    
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
            parent, 'end', 
            text="{} - {}".format(
                analysisResult.GetAnalysisType(),
                analysisResult.Media.GetFileName()
            ),
            values=(
                 analysisResult.Media.GetFileName(),
                 analysisResult.Media.BasePath,
                 analysisResult.Media.ParentDirectory
            )
        )
        
        return newNode
        