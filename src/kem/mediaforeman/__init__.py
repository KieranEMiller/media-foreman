import sys
import os
import inspect
import logging
import logging.config

'''get the name of this file; have to use this method as opposed
to the __file__ property since this is running as main and 
not a class or module'''
currentDir = os.path.dirname(inspect.getfile(inspect.currentframe()))

'''go up 2 directories from this init script, which is the base folder 
for the app right under src'''
logPath = os.path.abspath(os.path.join(currentDir, "..", "..", "mediaforeman.log"))

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
            'level': "INFO",
            'formatter': 'my_formatter',
            'filename': logPath,
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