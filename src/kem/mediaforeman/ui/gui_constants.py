class GUIConstants(object):

    '''
    padding is used for window and control padding
    sometimes at different multiples, for example window padding is a 
    3*the x/y padding
    '''
    PADDING_X = 5
    PADDING_Y = 5

    RESULTS_TAB_HEADER_ALLANALYSES = "All Analyses"
    RESULTS_TAB_HEADER_FILEANALYSES = "File Analyses"
    RESULTS_TAB_HEADER_COLLANALYSES = "Collection Analyses"

    RESULTS_TREE_COLUMN_HEADER_FILENAME = "File Name"
    RESULTS_TREE_COLUMN_HEADER_PATH = "Path"
    RESULTS_TREE_COLUMN_HEADER_PARENT_DIR = "Parent Dir"

    '''used to highlight rows that contain errors'''
    RESULTS_TREE_TAG_HAS_ISSUES = "HasIssues"
    RESULTS_TREE_TAG_HAS_NOISSUES = "HasNoIssues"
    RESULTS_TREE_TAG_HAS_ISSUES_COLOR = "coral1"
    RESULTS_TREE_TAG_HAS_NOISSUES_COLOR = "pale green"
    
    def __init__(self, params):
        pass