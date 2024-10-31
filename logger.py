import logging
import logging.handlers

# logger = logging.getLogger(__name__)
logger = logging.getLogger('foo-loger')
# print(__name__)
# print(logger)

# def namer(name):
#     return name + ".gz"

# def rotator(source, dest):
#     with open(source, 'rb') as f_in:
#         with gzip.open(dest, 'wb') as f_out:
#             shutil.copyfileobj(f_in, f_out)
#     os.remove(source)


# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')



logger.setLevel(logging.DEBUG)

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)

fileHandler = logging.FileHandler('log123.txt', mode='a', encoding='utf-8')

rotatingHandler = logging.handlers.RotatingFileHandler('rotlog.txt', mode='w', maxBytes=200, backupCount=5)
# rotatingHandler.rotator
# rotatingHandler.namer
rotatingHandler.setFormatter(formatter)

logger.addHandler(streamHandler)
logger.addHandler(fileHandler)
logger.addHandler(rotatingHandler)

logger.info("info from logger")

for i in range(30):
    logger.info(f'Log message {i}')