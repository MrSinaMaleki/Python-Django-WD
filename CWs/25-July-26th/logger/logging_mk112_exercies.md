## 1. Formatting your logs
1. Create a custom format that includes the timestamp, log level, and message.
2. Use this format in the basic configuration.
3. Log a few messages and observe the output format.
[quick reference on different logrecord attributes **{}-formatting,**](https://docs.python.org/3/library/logging.html#logrecord-attributes)



## 2. What is the difference betweeen `logging.error` and `logging.exception`

1. Create a function that will raise an error (for example a ZeroDivisionError)
2. now I need you to log the error + the traceback
3. see the difference between the two `error()` and `exception()` methods inside a *try...except* code block.


## 3. loggers
1. create a project.
    - example project setup
```css
my_project/
│
├── module1.py
├── module2.py
└── main.py
```
2. create a logger for each file
3. format the log in such way that the logger for each module shows the name of the file that is being logged. example log:
```log
file2 - file2.py - 2024-07-26 12:37:49 - DEBUG - Starting data analysis in module2
file2 - file2.py - 2024-07-26 12:37:49 - INFO - Data analysis completed successfully in module2
main - main.py - 2024-07-26 12:37:49 - INFO - Main application finished
```
4. have two handlers. one that writes to console and another that saves the logs in a file called `application.log`.

## 4. Log Rotation
Run this code (several times - and watch inside the files that are being created), then try to explain what this bit of code is doing.
- *hint*: Research Log Rotation and explain why this code can be useful?

```py
import logging
from logging.handlers import RotatingFileHandler
import random


handler = RotatingFileHandler('rotating.log', maxBytes=200, backupCount=3)
logger = logging.getLogger('RotatingLogger')
logger.setLevel(logging.INFO)
logger.addHandler(handler)

for i in range(100):
    logger.info(f'Log message {random.random()}')
```

## 5. complete this code so that it prints this result:

```python 
import logging
import logging.config

config = {
    'version': 1,
    'formatters': {
        'default': {
            'format': ''
        }
    },
    '': {
        'console': {
            'class': 'logging.StreamHandler',
            '': 'DEBUG',
            'formatter': 'default',
        },
        'file': {
            'class': '', # logs in complex.log
            'filename': 'complex.log',
            'level': 'INFO',
            'formatter': 'default',
        },
    },
    'loggers': {
        '': { 
            'level': '',
            'handlers': ,
        },
    }
}

logging.config.dictConfig(config)

logging.debug('Debug message')
logging.info('Info message')
```
result:
```log
2024-07-26 12:40:59,029 - root - DEBUG - Debug message
2024-07-26 12:40:59,029 - root - INFO - Info message
```
