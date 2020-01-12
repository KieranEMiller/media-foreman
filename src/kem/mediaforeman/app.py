'''
Created on Dec 29, 2019

@author: kieranemiller
'''
import logging

from kem.mediaforeman.ui.console_app import ConsoleApp
from kem.mediaforeman.ui.gui import GuiApp

if __name__ == '__main__':
    
    _log = logging.getLogger()
    _log.info("app startup")
    
    welcomeMsg = "media foreman: manage and maintain media files and metadata\n" 
    _log.info(welcomeMsg)
    
    app = ConsoleApp()
    if(app._args.gui):
        gui = GuiApp()
        gui.Run()
    else:
        app.Run()
    