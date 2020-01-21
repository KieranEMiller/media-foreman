from tkinter import *
from tkinter import ttk

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
        
        