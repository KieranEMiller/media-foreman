from tkinter import *
from tkinter import ttk
from kem.mediaforeman.analyses.analysis_type import AnalysisType
import tkinter
from kem.mediaforeman.ui.gui_config import ConfigWindow
from kem.mediaforeman.app_config import AppConfig

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
        
    def Run(self):

        self._rootFrame = self.SetupRootFrame()
        
        self.SetupConfigSection()
        separator = ttk.Separator(self._rootFrame, orient=HORIZONTAL)
        separator.grid(row=2, columnspan=2, pady=5)
        self._resultsByAnalysisType = self.SetupResultsTabs()
        
        self._window.mainloop() 
        
    def SetupRootFrame(self):
        rootFrame = Frame(self._window, padx=10, pady=10)
        rootFrame.grid(row=0,column=0, columnspan=2, rowspan=3, sticky=N+E+S+W)

        Grid.rowconfigure(rootFrame, 3, weight=1)
        Grid.columnconfigure(rootFrame, 1, weight=1)
        
        return rootFrame
    
    def SetupConfigSection(self):
        topFrame = Frame(self._rootFrame)
        topFrame.grid(row=0, column=0, columnspan=2, rowspan=1, sticky=W+E)
        Grid.columnconfigure(topFrame, 1, weight=1)
        
        rootDirLabel = Label(topFrame, text='Root Directory')
        rootDirLabel.grid(row=0, column=0, columnspan=1, sticky=W)
 
        rootDirInput = Entry(topFrame)
        rootDirInput.grid(row=0, column=1, columnspan=2, sticky=W+E) 
        Grid.columnconfigure(rootDirInput, 1, weight=1)

        processBtn = Button(topFrame, text="Process Root")
        processBtn.grid(row=1, column=1, sticky=E)

        configBtn = Button(topFrame, text="Configuration", command=self.ShowConfig)
        configBtn.grid(row=1, column=0, sticky=W)
        
    def ShowConfig(self):
        win = ConfigWindow(self, self._window)
        
    def UpdateConfigFromConfigWindow(self, config):
        '''currently only the types of analyses performed are updated
        or available on the configuration GUI, so just update those'''
        self._config.AnalysesToRun = []
        self._config.AnalysesToRun.extend(config.AnalysesToRun)
        

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
        
        tree = ttk.Treeview(tabFrame, columns=('FileName', 'Path', 'ParentDirectory'))

        '''setup a vertical scrollbar'''
        vsb = ttk.Scrollbar(tabFrame, orient="vertical")
        vsb.configure(command=tree.yview)
        vsb.grid(row=0, rowspan=2, column=2, sticky=N+S)
        tree.configure(yscrollcommand=vsb.set)

        tree.heading('#0', text='AnalysisType')
        tree.heading('#1', text='FileName')
        tree.heading('#2', text='Path')
        tree.heading('#3', text='ParentDirectory')
        tree.column('#0', width=100, stretch=tkinter.NO)
        tree.column('#1', width=100, stretch=tkinter.NO)
        tree.column('#2', stretch=tkinter.YES)
        tree.column('#3', stretch=tkinter.YES)
        tree.grid(row=1, columnspan=2, sticky='nsew')
        
        return tabFrame
        
        ''' insertion sample
        for i in range(50):
            parent = tree.insert('', 'end', text='item num ' + str(i), values=('qwer', 'qwer', 'qwer'))
            for z in range(5):
                tree.insert(parent, 'end', text='item num ' + str(z), values=('qwer', 'qwer', 'qwer'))
        
        '''