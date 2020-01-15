from tkinter import *

class GuiApp(object):

    def __init__(self):
        self._tk = Tk()
        self._tk.title("Media Foreman GUI")
        self._tk.geometry("400x400")
    
    def Run(self):
        rootDirLabel = Label(self._tk, text='First Name')
        rootDirLabel.grid(row=0) 
        
        rootDirInput = Entry(self._tk) 
        rootDirInput.grid(row=0, column=1) 
        
        
        
        self._tk.mainloop() 