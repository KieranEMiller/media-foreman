from tkinter import *
from tkinter import ttk
from kem.mediaforeman.analyses.analysis_type import AnalysisType
import tkinter
from kem.mediaforeman.ui.gui_config import ConfigWindow
from kem.mediaforeman.app_config import AppConfig
from tkinter.scrolledtext import ScrolledText
from kem.mediaforeman.ui.gui_constants import GUIConstants
from kem.mediaforeman.media_root_directory import MediaRootDirectory
from kem.mediaforeman.media_analyzer import MediaAnalyzer
from kem.mediaforeman.ui.gui_results_tree_item_factory import GUIResultsTreeItemFactory
from tkinter.ttk import Style
from kem.mediaforeman.media_collection import MediaCollection
from kem.mediaforeman.analyses.analysis_type_factory import AnalysisTypeFactory

class GuiApp(object):

    def __init__(self):
        self._config = AppConfig()
        
        self._window = Tk()
        self._window.title("Media Foreman")
        self._window.geometry("500x350")
        
        Grid.rowconfigure(self._window, 1, weight=1)
        Grid.columnconfigure(self._window, 1, weight=1)
        
        '''the root container for all window controls'''
        self._rootFrame = None
        self._resultTrees = None
        
        '''the text control that displays the running configuration'''
        self._configText = None
        
        '''the input control for the root directory'''
        self._rootDirInput = None
        
        '''
        background color fix: this resolves an issue where the tags
        for tree view items are not handled properly in the version of tkinter
        tree view style fix taken from: 
        https://bugs.python.org/issue36468
        '''
        style = ttk.Style()
        style.map('Treeview', foreground=self.fixed_map('foreground'), background=self.fixed_map('background'))
        
    def Run(self):
        self._rootFrame = self.SetupRootFrame()
        
        self.SetupConfigSection()
        
        separator = ttk.Separator(self._rootFrame, orient=HORIZONTAL)
        separator.grid(row=2, columnspan=2, pady=GUIConstants.PADDING_Y)
        
        self._resultTrees = self.SetupResultsTabs()
        
        self._window.mainloop() 
    
    def ShowConfig(self):
        '''TODO: note that every time the config window is shown it comes in
        as blank; need a way to update the window with the current running config
        each time it is shown'''
        win = ConfigWindow(self, self._window)
        
    def UpdateConfigFromConfigWindow(self, config):
        '''currently only the types of analyses performed are updated
        or available on the configuration GUI, so just update those'''
        self._config.AnalysesToRun = []
        self._config.AnalysesToRun.extend(config.AnalysesToRun)
        
        '''refresh the config display'''
        self.UpdateConfigDisplayBox()
        
    def UpdateConfigDisplayBox(self):
        self._configText.delete('1.0', END)
        self._configText.insert('1.0', self._config.PrintConfig())
        
    def ProcessRootDirs(self):
        self.ResetResultsTree()
        
        self._config.RootDirectories = [self._rootDirInput.get()]
        processor = MediaRootDirectory(self._config.RootDirectories)
        media = processor.Process()
        
        analyzer = MediaAnalyzer(media, self._config.AnalysesToRun)
        summary = analyzer.Analyze(self._config.SummarizeOnly)
        
        self.ShowResults(summary)
            
    def ShowResults(self, summary):
        itemFactory = GUIResultsTreeItemFactory()
        analysisFactory = AnalysisTypeFactory()
        
        for analysis in summary.AnalysisResultsByAnalysisType:
            
            analysisResults = summary.AnalysisResultsByAnalysisType[analysis]

            resultTrees = [self._resultTrees[GUIConstants.RESULTS_TAB_HEADER_ALLANALYSES]]
            thisTree = self._resultTrees[GUIConstants.RESULTS_TAB_HEADER_ALLANALYSES]
            
            analysisClass = analysisFactory.TypeToAnalysis(analysis)()
            if(analysisClass.IsCollectionAnalysis()):
                resultTrees.append(self._resultTrees[GUIConstants.RESULTS_TAB_HEADER_COLLANALYSES])

            elif(analysisClass.IsFileAnalysis()):
                resultTrees.append(self._resultTrees[GUIConstants.RESULTS_TAB_HEADER_FILEANALYSES])
                
            if(sum([1 for result in analysisResults if result.HasIssues == True]) > 0):
                resultTrees.append(self._resultTrees[GUIConstants.RESULTS_TAB_HEADER_HAS_ISSUES])
            else:
                resultTrees.append(self._resultTrees[GUIConstants.RESULTS_TAB_HEADER_NO_ISSUES])
                
            for thisTree in resultTrees:
                parentItem = itemFactory.AddParentToResultsTree(
                    thisTree, analysis, analysisResults
                )
                
                for analysisResult in analysisResults:
                    item = itemFactory.AddAnalysisToResultsTree(thisTree, analysisResult, parentItem)
                

    def ResetResultsTree(self):
        for tab in self._resultTrees:
            tree = self._resultTrees[tab]
            for item in tree.get_children():
                tree.delete(item)

    def SetupRootFrame(self):
        rootFrame = Frame(self._window, padx=GUIConstants.PADDING_X*2, pady=GUIConstants.PADDING_Y*2)
        rootFrame.grid(row=0,column=0, columnspan=2, rowspan=3, sticky=N+E+S+W)

        Grid.rowconfigure(rootFrame, 3, weight=1)
        Grid.columnconfigure(rootFrame, 1, weight=1)
        
        return rootFrame
    
    def SetupConfigSection(self):
        topFrame = Frame(self._rootFrame)
        topFrame.grid(row=0, column=0, columnspan=3, rowspan=1, sticky=W+E)
        Grid.columnconfigure(topFrame, 1, weight=1)
        
        rootDirLabel = Label(topFrame, text='Root Directory')
        rootDirLabel.grid(row=0, column=0, columnspan=1, sticky=W, padx=GUIConstants.PADDING_X)
 
        self._rootDirInput = Entry(topFrame)
        self._rootDirInput.grid(row=0, column=1, columnspan=3, sticky=W+E) 
        Grid.columnconfigure(self._rootDirInput, 1, weight=1)

        processBtn = Button(topFrame, text="Process Root", command=self.ProcessRootDirs)
        processBtn.grid(row=1, column=2, sticky=E, padx=GUIConstants.PADDING_X)

        configBtn = Button(topFrame, text="Configuration", command=self.ShowConfig)
        configBtn.grid(row=1, column=0, sticky=W, padx=GUIConstants.PADDING_X)
        
        self._configText = ScrolledText(topFrame, height=3)
        self._configText.grid(row=1, column=1, sticky=W+E)
        
    def SetupResultsTabs(self):
        frame = Frame(self._rootFrame)
        frame.grid(row=3, column=0, columnspan=2,sticky=N+E+S+W)
        Grid.columnconfigure(frame, 1, weight=1)

        tabControl = ttk.Notebook(frame)
        tabControl.pack(expand=1, fill='both')
        
        tabsByAnalysisType = {}
        tabsByAnalysisType[GUIConstants.RESULTS_TAB_HEADER_ALLANALYSES] = self.SetupResultsTab(tabControl, GUIConstants.RESULTS_TAB_HEADER_ALLANALYSES)
        tabsByAnalysisType[GUIConstants.RESULTS_TAB_HEADER_FILEANALYSES] = self.SetupResultsTab(tabControl, GUIConstants.RESULTS_TAB_HEADER_FILEANALYSES)
        tabsByAnalysisType[GUIConstants.RESULTS_TAB_HEADER_COLLANALYSES] = self.SetupResultsTab(tabControl, GUIConstants.RESULTS_TAB_HEADER_COLLANALYSES)
        tabsByAnalysisType[GUIConstants.RESULTS_TAB_HEADER_HAS_ISSUES] = self.SetupResultsTab(tabControl, GUIConstants.RESULTS_TAB_HEADER_HAS_ISSUES)
        tabsByAnalysisType[GUIConstants.RESULTS_TAB_HEADER_NO_ISSUES] = self.SetupResultsTab(tabControl, GUIConstants.RESULTS_TAB_HEADER_NO_ISSUES)
        return tabsByAnalysisType
    
    def SetupResultsTab(self, tabControl, tabName):
        tabFrame = ttk.Frame(tabControl)
        Grid.columnconfigure(tabFrame, 1, weight=1)
        Grid.rowconfigure(tabFrame, 1, weight=1)
        tabControl.add(tabFrame, text=tabName)
        
        lbl1 = Label(tabFrame, text=tabName)
        lbl1.grid(column=0, row=0)
        
        tree = ttk.Treeview(tabFrame, columns=(
            GUIConstants.RESULTS_TREE_COLUMN_HEADER_FILENAME, 
            GUIConstants.RESULTS_TREE_COLUMN_HEADER_PATH, 
            GUIConstants.RESULTS_TREE_COLUMN_HEADER_PARENT_DIR
        ))

        '''setup a vertical scrollbar'''
        vsb = ttk.Scrollbar(tabFrame, orient="vertical")
        vsb.configure(command=tree.yview)
        vsb.grid(row=0, rowspan=2, column=2, sticky=N+S)
        tree.configure(yscrollcommand=vsb.set)

        tree.heading('#0', text='AnalysisType')
        tree.heading('#1', text=GUIConstants.RESULTS_TREE_COLUMN_HEADER_FILENAME)
        tree.heading('#2', text=GUIConstants.RESULTS_TREE_COLUMN_HEADER_PATH)
        tree.heading('#3', text=GUIConstants.RESULTS_TREE_COLUMN_HEADER_PARENT_DIR)
        tree.column('#0', width=300, stretch=tkinter.NO)
        tree.column('#1', width=100, stretch=tkinter.NO)
        tree.column('#2', stretch=tkinter.YES)
        tree.column('#3', stretch=tkinter.YES)
        tree.grid(row=1, columnspan=2, sticky=N+S+E+W)

        tree.tag_configure(
            GUIConstants.RESULTS_TREE_TAG_HAS_ISSUES, 
            background=GUIConstants.RESULTS_TREE_TAG_HAS_ISSUES_COLOR
        )

        tree.tag_configure(
            GUIConstants.RESULTS_TREE_TAG_HAS_NOISSUES, 
            background=GUIConstants.RESULTS_TREE_TAG_HAS_NOISSUES_COLOR
        )
        
        return tree

    '''
    background color fix: this resolves an issue where the tags
    for tree view items are not handled properly in the version of tkinter
    tree view style fix taken from: 
    https://bugs.python.org/issue36468
    '''
    def fixed_map(self, option):
        # Fix for setting text colour for Tkinter 8.6.9
        # From: https://core.tcl.tk/tk/info/509cafafae
        #
        # Returns the style map for 'option' with any styles starting with
        # ('!disabled', '!selected', ...) filtered out.

        # style.map() returns an empty list for missing options, so this
        # should be future-safe.
        style = ttk.Style()
        return [elm for elm in style.map('Treeview', query_opt=option) if
          elm[:2] != ('!disabled', '!selected')]