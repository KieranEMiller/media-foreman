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
        self._resultsByAnalysisType = None
        
        '''the text control that displays the running configuration'''
        self._configText = None
        
    def Run(self):

        self._rootFrame = self.SetupRootFrame()
        
        self.SetupConfigSection()
        separator = ttk.Separator(self._rootFrame, orient=HORIZONTAL)
        separator.grid(row=2, columnspan=2, pady=GUIConstants.PADDING_Y)
        self._resultsByAnalysisType = self.SetupResultsTabs()
        
        self._window.mainloop() 
        
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
 
        rootDirInput = Entry(topFrame)
        rootDirInput.grid(row=0, column=1, columnspan=3, sticky=W+E) 
        Grid.columnconfigure(rootDirInput, 1, weight=1)

        processBtn = Button(topFrame, text="Process Root", command=self.ProcessRootDirs)
        processBtn.grid(row=1, column=2, sticky=E, padx=GUIConstants.PADDING_X)

        configBtn = Button(topFrame, text="Configuration", command=self.ShowConfig)
        configBtn.grid(row=1, column=0, sticky=W, padx=GUIConstants.PADDING_X)
        
        self._configText = ScrolledText(topFrame, height=3)
        self._configText.grid(row=1, column=1, sticky=W+E)
        
    def ShowConfig(self):
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
        processor = MediaRootDirectory(self._config.RootDirectories)
        media = processor.Process()
        
        analyzer = MediaAnalyzer(media, self._config.AnalysesToRun)
        summary = analyzer.Analyze(self._config.SummarizeOnly)
        
    def SetupResultsTabs(self):
        frame = Frame(self._rootFrame)
        frame.grid(row=3, column=0, columnspan=2,sticky=N+E+S+W)
        Grid.columnconfigure(frame, 1, weight=1)

        tabControl = ttk.Notebook(frame)
        tabControl.pack(expand=1, fill='both')
        
        tabsByAnalysisType = {}
        tabsByAnalysisType["AllAnalyses"] = self.SetupResultsTab(tabControl, "AllAnalyses")
        tabsByAnalysisType["FileAnalyses"] = self.SetupResultsTab(tabControl, "FileAnalyses")
        tabsByAnalysisType["CollectionAnalyses"] = self.SetupResultsTab(tabControl, "CollectionAnalyses")
            
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
        tree.column('#0', width=100, stretch=tkinter.NO)
        tree.column('#1', width=100, stretch=tkinter.NO)
        tree.column('#2', stretch=tkinter.YES)
        tree.column('#3', stretch=tkinter.YES)
        tree.grid(row=1, columnspan=2, sticky=N+S+E+W)
        
        return tabFrame
        