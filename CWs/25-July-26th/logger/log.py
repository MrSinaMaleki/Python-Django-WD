import logging

# Q1
# logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
# logging.critical("This is a an error")


# timestamp- log level - message


# Q2

# def dev(a=10, b=0):
#     return a / b
#
#
# try:
#     dev()
# except Exception as e:
#     # logging.exception("The following exception has occurred (%s)", e)
#     logging.error("The following error has occurred (%s) ", e)

# Exception shows the trace-back but logging.error just shows the message.


# Q3 No answer

# Q4
import logging
from logging.handlers import RotatingFileHandler
import random


handler = RotatingFileHandler('rotating.log', maxBytes=200, backupCount=10)
logger = logging.getLogger('RotatingLogger')
logger.setLevel(logging.INFO)
logger.addHandler(handler)

for i in range(100):
    logger.info(f'{i}Log message {random.random()}')
    print(i)


# Log rotation is an automated process of managing log file size, preventing the logs from filling the storage space and slowing down the system
# if there is not enough space its save the last logs.
#  maxBytes=200 -> size of each rotating.log file.
#  backupCount=10 -> numer of files that program can make.



# Q5:

# import logging.config
#
# logger = logging.getLogger(__name__)
#
# config = {
#     'version': 1,
#     'formatters': {
#         'default': {
#             'format': ''
#         }
#     },
#     '': {
#         'console': {
#             'class': 'logging.StreamHandler',
#             '': 'DEBUG',
#             'formatter': 'default',
#         },
#         'file': {
#             'class': '',  # logs in complex.log
#             'filename': 'complex.log',
#             'level': 'INFO',
#             'formatter': 'default',
#         },
#     },
#     'loggers': {
#         '': {
#             'level': 10,
#             'handlers': '',
#         },
#     }
# }
#
# custom_handler = logging.StreamHandler()
#
# logging.config.dictConfig(config)
# logger.addHandler(custom_handler)
#
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
#
# logging.debug('Debug message')
# logging.info('Info message')
