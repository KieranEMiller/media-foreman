from tkinter import *
from tkinter import ttk

from kem.mediaforeman.analyses.analysis_type import AnalysisType
from kem.mediaforeman.app_config import AppConfig
from kem.mediaforeman.ui.gui_constants import GUIConstants
from kem.mediaforeman.analyses.analysis_type_factory import AnalysisTypeFactory

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
        
        typeFactory = AnalysisTypeFactory()
        for analysis in self._analyses:
            if(self._analyses[analysis].get() == 1):
                '''here the array is an instance of each analysis type'''
                config.AnalysesToRun.append(typeFactory.TypeToAnalysis(analysis)())
        
        self._app.UpdateConfigFromConfigWindow(config)
        
    def InitWindowSizeAndLocationFromParent(self, parent):
        self._window.geometry("%dx%d+%d+%d" % 
                              (parent.winfo_width() - (GUIConstants.PADDING_X*3), 
                               parent.winfo_height() - (GUIConstants.PADDING_Y*3), 
                               parent.winfo_x() + GUIConstants.PADDING_X*2, 
                               parent.winfo_y() + GUIConstants.PADDING_Y*2)
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

        '''the max number needs work - currently if the user resizes the parent
        or main window, the config window is increased similarly but the
        checkbox grid does not resize causing all the controls to be grouped 
        in the top left of the window'''
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