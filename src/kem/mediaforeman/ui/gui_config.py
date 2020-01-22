from tkinter import *
from tkinter import ttk
from kem.mediaforeman.analyses.analysis_type import AnalysisType

class ConfigWindow(object):

    def __init__(self, parent):
        self._window = Toplevel(parent)
        self._window.wm_title("Media Foreman Configuration")
        
        WIN_X_BUFFER = 20
        WIN_Y_BUFFER = 30
        
        self._window.geometry("%dx%d+%d+%d" % 
                              (parent.winfo_width() - (2*WIN_X_BUFFER), 
                               parent.winfo_height() - (2*WIN_Y_BUFFER), 
                               parent.winfo_x() + WIN_X_BUFFER, 
                               parent.winfo_y() + WIN_Y_BUFFER)
        )
        
        '''prevent parent from being interacted with'''
        self._window.grab_set()
        self.SetupControls()
        self._window.focus()
        
    def SetupControls(self):
        self._rootFrame = self.SetupRootFrame()
        
        rootDirLabel = Label(self._rootFrame, text='Run These Analyses')
        rootDirLabel.grid(row=0, column=0)
        
        MAX_CHECKBOXES_PER_ROW = 2
        row = 0
        column=0
        
        for analysis in AnalysisType:
            checkbox = Checkbutton(self._rootFrame, text=analysis.name, variable=True)
            checkbox.grid(row=row, column=column, sticky=W)
            
            column=column+1
            if(column>=MAX_CHECKBOXES_PER_ROW): 
                row = row + 1
                column = 0
        
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
        