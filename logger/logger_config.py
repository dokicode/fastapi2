

class Logger():

    def __init__(self, path_to_log_file) -> None:
        self.path_to_log_file = path_to_log_file

    def getConfig(self):
        logger_config = {
            "version": 1,
            # "disable_existing_loggers": True,
            "formatters": {
                "default": {
                    "()": "uvicorn.logging.DefaultFormatter",
                    "fmt": "%(asctime)s %(levelname)s %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M:%S",

                },
            },
            # "namer": lambda name: name.replace(".log", "") + ".log",
            "handlers": {
                'default': {
                    'formatter': 'default',
                    'class': 'logging.StreamHandler',
                },
                'file_handler': {
                    # 'level': 'INFO',
                    'formatter': 'default',
                    'class': 'logging.FileHandler',
                    'filename': self.path_to_log_file,
                    'mode': 'a',
                },
                # 'rotating_file_handler': {
                #     # 'level': 'DUBUG',
                #     'formatter': 'default',
                #     'class': 'logging.handlers.RotatingFileHandler',
                #     # 'class': 'logging.RotatingFileHandler',
                #     'filename': self.path_to_log_file,
                #     'mode': 'a',
                #     'maxBytes': 500,
                #     'backupCount': 10,
                # },
                # 'time_rotating_file_handler': {
                #     'formatter': 'default',
                #     'class': 'logging.handlers.TimedRotatingFileHandler',
                #     'filename': self.path_to_log_file,
                #     # 'when': 'midnight',
                #     'when': 'M',
                #     'interval': 5,
                #     'delay': False
                # },
                # 'concurent_time_rotation_file_handler': {
                #     'class': 'concurrent_log_handler.ConcurrentTimedRotatingFileHandler',
                #     'formatter': 'default',
                #     'filename': self.path_to_log_file,
                #     'mode': 'a',
                #     'when': 'M',
                #     'interval': 1,
                #     'delay': False,
                #     'level': "DEBUG"

                    # 'namer': eval(lambda name: name.replace(".log", "") + ".log")
                    # 'args': (self.path_to_log_file, 'a'),
                # }
            },
            "root": {
                # "handlers": ["file_handler"],
                # "handlers": ["default", "concurent_time_rotation_file_handler"],
                "handlers": ["default", "file_handler"],
                "level": "DEBUG",
                "propagate": True,
                # 'namer': lambda name: name.replace(".log", "") + ".log"
            }
        }
        return logger_config
