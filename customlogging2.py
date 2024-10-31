# https://stackoverflow.com/questions/63510041/adding-python-logging-to-fastapi-endpoints-hosted-on-docker-doesnt-display-api

log_config = {
    "version": 1,
    # "disable_existing_loggers": True,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(asctime)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",

        },
    },
    "handlers": {
        # "default": {
        #     "formatter": "default",
        #     "class": "logging.StreamHandler",
        #     # "class": "handlers.RotatingFileHandler",
        #     # "args": "('logfile222.log','a')",
        #     "stream": "ext://sys.stderr",
        # },
        # 'info_rotating_file_handler': {
        #     'level': 'INFO',
        #     'formatter': 'default',
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'filename': 'info.log',
        #     'mode': 'a',
        #     'maxBytes': 1048576,
        #     'backupCount': 10,
        # },
        'default': {
            'formatter': 'default',
            'class': 'logging.StreamHandler',
        },
        'error_file_handler': {
            # 'level': 'INFO',
            # 'formatter': 'default',
            'class': 'logging.FileHandler',
            'filename': 'error.log',
            'mode': 'a',
        },
    },
    "root": {
        "handlers": ["default", "error_file_handler"],
        "level": "INFO",
        "propagate": True,

    },
    # "loggers": {
    #     "foo-logger": {"handlers": ["error_file_handler"], "level": "DEBUG"},
    # },
}


if __name__ == "__main__":
    print('Main')
    import logging
    from logging import config
    from logging.config import dictConfig

    config.dictConfig(log_config)


    logger = logging.getLogger("foo-logger")
    logger.info("hello")
    logger.info("hello2")
    logger.error("hello error")