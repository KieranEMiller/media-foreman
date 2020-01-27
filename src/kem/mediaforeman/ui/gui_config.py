from tkinter import *
from tkinter import ttk
from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.app_config import AppConfig

class ConfigWindow(object):

    def __init__(self, app, parentWindow):
        self._app = app
        self._parent = parentWindow
        
        self._config = AppConfig()
        self._window = Toplevel(parentWindow)
        self._window.wm_title("Media Foreman Configuration")
        
        self.InitWindowSizeAndLocationFromParent(parentWindow)
        
        '''prevent parent from being interacted with'''
        self._window.grab_set()
        
        self.SetupControls()
        self._window.focus()
        
        self._window.protocol("WM_DELETE_WINDOW", self.OnWindowClosingEvent)
        
    def OnWindowClosingEvent(self):
        self.UpdateConfigOnParent()
        self._window.destroy()
        
    def UpdateConfigOnParent(self):
        config = AppConfig()
        
        for analysis in self._analyses:
            if(self._analyses[analysis].get() == 1):
                config.AnalysesToRun.append(analysis)
        
        self._app.UpdateConfigFromConfigWindow(config)
        
    def InitWindowSizeAndLocationFromParent(self, parent):
        WIN_X_BUFFER = 20
        WIN_Y_BUFFER = 30
        
        self._window.geometry("%dx%d+%d+%d" % 
                              (parent.winfo_width() - (2*WIN_X_BUFFER), 
                               parent.winfo_height() - (2*WIN_Y_BUFFER), 
                               parent.winfo_x() + WIN_X_BUFFER, 
                               parent.winfo_y() + WIN_Y_BUFFER)
        )
        
    def SetupControls(self):
        self._rootFrame = self.SetupRootFrame()

        self.SetupAnalysisListControls()
        
    def SetupRootFrame(self):
        rootFrame = Frame(self._window, padx=10, pady=10)
        rootFrame.grid(row=0,column=0, columnspan=1, rowspan=3, sticky=N+E+S+W)

        Grid.rowconfigure(rootFrame, 0, weight=1)
        Grid.columnconfigure(rootFrame, 0, weight=1)

        '''
        vsb = ttk.Scrollbar(rootFrame, orient="vertical")
        vsb.configure(command=rootFrame.yview)
        vsb.grid(row=0, rowspan=2, column=2, sticky=N+S)
        rootFrame.configure(yscrollcommand=vsb.set)
        '''
        
        return rootFrame
        
    def SetupAnalysisListControls(self):
        
        self._analyses = {}
        
        rootDirLabel = Label(self._rootFrame, text='Run These Analyses')
        rootDirLabel.grid(row=0, column=0, sticky=W)

        MAX_CHECKBOXES_PER_ROW = 2
        row = 1
        column=0
        
        for analysis in AnalysisType:
            self._analyses[analysis] = IntVar()
            self._analyses[analysis].set(0)
            
            checkbox = Checkbutton(self._rootFrame, text=analysis.name, variable=self._analyses[analysis] )
            checkbox.grid(row=row, column=column, sticky=W)
            
            column=column+1
            if(column>=MAX_CHECKBOXES_PER_ROW): 
                row = row + 1
                column = 0