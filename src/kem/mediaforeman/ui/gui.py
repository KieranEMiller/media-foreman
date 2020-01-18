from tkinter import *
from tkinter import ttk
from kem.mediaforeman.analyses.analysis_type import AnalysisType
import tkinter

class GuiApp(object):

    def __init__(self):
        self._window = Tk()
        self._window.title("Media Foreman")
        self._window.geometry("500x350")
        Grid.rowconfigure(self._window, 1, weight=1)
        Grid.columnconfigure(self._window, 1, weight=1)
        
        '''the root container for all window controls'''
        self._rootFrame = None
        self._resultsTabsByAnalysisType = None
        
    def Run(self):

        self._rootFrame = self.SetupRootFrame()
        
        self.SetupConfigSection()
        self._resultsTabsByAnalysisType = self.SetupResultsTabs()
        
        self._window.mainloop() 
        
    def SetupRootFrame(self):
        rootFrame = Frame(self._window, padx=10, pady=10)
        rootFrame.grid(row=0,column=0, columnspan=2, rowspan=3, sticky=N+E+S+W)

        Grid.rowconfigure(rootFrame, 2, weight=1)
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

    def SetupResultsTabs(self):
        frame = Frame(self._rootFrame)
        frame.grid(row=2, column=0, columnspan=2,sticky=N+E+S+W)
        Grid.columnconfigure(frame, 1, weight=1)

        tabControl = ttk.Notebook(frame)
        
        tabsByAnalysisType = {}
        for analysisType in AnalysisType:
            tabFrame = ttk.Frame(tabControl)
            Grid.columnconfigure(tabFrame, 1, weight=1)
            Grid.rowconfigure(tabFrame, 1, weight=1)
            tabControl.add(tabFrame, text=analysisType.name)
            
            lbl1 = Label(tabFrame, text=analysisType.name)
            lbl1.grid(column=0, row=0)
            
            tree = ttk.Treeview(tabFrame, columns=('FileName', 'Path', 'ParentDirectory'))

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
            
            for i in range(50):
                parent = tree.insert('', 'end', text='item num ' + str(i), values=('qwer', 'qwer', 'qwer'))
                for z in range(5):
                    tree.insert(parent, 'end', text='item num ' + str(z), values=('qwer', 'qwer', 'qwer'))
            
            tabsByAnalysisType[analysisType] = tabFrame
            
        tabControl.pack(expand=1, fill='both')
        return tabControl
    
    