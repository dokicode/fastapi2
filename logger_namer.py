import os

import logging
from logging.config import dictConfig

from logger.logger_config import Logger


path_to_log_file = os.path.join('./logs2', 'fastapi_TimedRotatingFileHandler.log')
loggerObj = Logger(path_to_log_file)

# print(log_config)

# dictConfig(log_config)

logger_conf = loggerObj.getConfig()
dictConfig(logger_conf)
log = logging.getLogger('root')
# print(log.handlers[0].namer)

log.handlers[1].namer = lambda name: name.replace(".log", "") + ".log"
# print(logger.handlers)



for i in range(10):
    log.info("test log")