'''
Created on Dec 29, 2019

@author: kieranemiller
'''
import logging
import logging.config
import sys
from kem.mediaforeman.console_app import ConsoleApp

if __name__ == '__main__':
    
    LOG_LEVEL = "DEBUG"
    
    config = {
        'version': 1,
        'formatters': {
            # Modify log message format here or replace with your custom formatter class
            'my_formatter': {
                'format': '(%(process)d) %(asctime)s %(name)s (line %(lineno)s) | %(levelname)s %(message)s'
            }
        },
        'handlers': {
            'console_stderr': {
                'class': 'logging.StreamHandler',
                'level': 'ERROR',
                'formatter': 'my_formatter',
                'stream': sys.stderr
            },
            'console_stdout': {
                'class': 'logging.StreamHandler',
                'level': 'WARN',
                'formatter': 'my_formatter',
                'stream': sys.stdout
            },
            'file': {
                # Sends all log messages to a file
                'class': 'logging.FileHandler',
                'level': 'DEBUG',
                'formatter': 'my_formatter',
                'filename': 'mediaforeman.log',
                'encoding': 'utf8'
            }
        },
        'root': {
            # In general, this should be kept at 'NOTSET'.
            # Otherwise it would interfere with the log levels set for each handler.
            'level': 'NOTSET',
            'handlers': ['console_stderr', 'console_stdout', 'file']
        },
    }

    logging.config.dictConfig(config)
    
    _log = logging.getLogger()
    _log.info("app startup")
    
    welcomeMsg = "media foreman: manage and maintain media files and metadata\n" 
    _log.info(welcomeMsg)
    print(welcomeMsg)
    
    app = ConsoleApp()
    app.Run()
    