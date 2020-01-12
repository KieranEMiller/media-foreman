from tkinter import *

class GuiApp(object):

    def __init__(self):
        self._tk = Tk()
    
    def Run(self):
        Label(self._tk, text='First Name').grid(row=0) 
        e1 = Entry(self._tk) 
        e1.grid(row=0, column=1) 
        
        self._tk.mainloop() 