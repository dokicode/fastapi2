# source: https://stackoverflow.com/questions/60715275/fastapi-logging-to-file
from gevent import monkey as curious_george
# monkey.patch_all()
curious_george.patch_all(thread=False, select=False)

import os
import sys
from typing import Union
import time
# https://stackoverflow.com/questions/22232201/how-in-python-find-where-exception-was-raised
import inspect


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder

from starlette.templating import Jinja2Templates

from starlette.requests import Request
from starlette.responses import Response

# https://stackoverflow.com/questions/61596911/catch-exception-globally-in-fastapi
from traceback import print_exception


import logging
from logging.config import dictConfig
# from concurrent_log_handler import ConcurrentTimedRotatingFileHandler

import uvicorn
from contextlib import asynccontextmanager

from DataService import DataService

# from customlogging2 import log_config
from logger.logger_config import Logger

import grequests



# dictConfig(log_config)

# print(__name__)
# print("logger", logging.getLogger(__name__))

# logger = logging.getLogger(__name__)
# logger = logging.getLogger("foo-logger")
# print(logger)
# logger.level("INFO")
# logger.info('test')

# app = FastAPI(debug=True)

path_to_log_file = os.path.join('./logs', 'fastapi_TimedRotatingFileHandler.log')
log_config = Logger(path_to_log_file).getConfig()
dictConfig(log_config)
logger = logging.getLogger('root')
logger.handlers[1].namer = lambda name: name.replace(".log", "") + ".log"


# print(logger.handlers)
# rh 
# print("Count handlers", logger)
# logger.namer = lambda name: name.replace(".log", "") + ".logs"
# logger.info('hello')
# dictConfig(log_config)



# log.info('Hello')
# def get_logger():
#     path_to_log_file = os.path.join('./logs', 'fastapi_TimedRotatingFileHandler.log')
#     logger = Logger(path_to_log_file)
#     return logger


templates = Jinja2Templates(directory='templates')
# app.logger = logger
# # Middleware
# @app.middleware('http')
# async def midlogger(request: Request, call_next):
#     print('mid')
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('+++Server started up!')
    yield
    logger.info('---Server shutting down!')


app = FastAPI(lifespan=lifespan, debug=True)
app.mount("/static", StaticFiles(directory='static'), name='static')





async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        # you probably want some kind of logging here
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print('exc_type', exc_value)

        # print_exception(e)
        # print(dir(exc_traceback))
        # logger.error(exc_traceback.tb_lineno)
        # print("Exception raised in %s" % inspect.trace())
        # print(inspect.trace()[-1])
        # print()
        logger.error(f"Caught an exception '{exc_value}' occured in {inspect.trace()[-1][1]}, line='{inspect.trace()[-1][2]}', function='{inspect.trace()[-1][3]}'")
        return Response("Internal server error", status_code=500)

app.middleware('http')(catch_exceptions_middleware)






# @app.on_event('startup')
# async def startup_event():
#     print('startup')
#     # logger = get_logger()
#     logger.info('Server started up!')

# @app.on_event('shutdown')
# def shutdown_event():
#     print('shutdown')
#     logger.info('Server shutting down!')

@app.get("/", response_class=HTMLResponse)
async def read_root(request:Request):
    # logger.error("hhjhjh")
    try:
        response = templates.TemplateResponse("index.html", context={"request": request})
    except Exception as e:
        response = e
    return response
    # return {"message": "Hello World!"}


# @app.get("/logme")
# async def logme(duration: str, module: str, name: str):
#     # print('duration', duration)
#     # logger.debug(f'duration {duration}')
#     # return duration
#     with open('prp.log', mode='a') as f:
#         f.write(f'{module} > {name}: {duration} s\n')
#         f.close()


@app.get("/logme")
async def logme(data: dict):
    # print('duration', duration)
    # logger.debug(f'duration {duration}')
    # return duration
    with open('prp.log', mode='a') as f:
        f.write(f'{data}\n\n')
        f.close()

@app.get("/grequests")
async def r_grequests():
    url = [
        'http://irkutskles.ru',
        'http://dondata.ru'
    ]

    rs = (grequests.get(u) for u in url)
    result = grequests.map(rs)

    # r = ({i, result[i].status_code} for i in result)
    # out = [item for item in r]
    # print('result', result[0].headers)
    return result[0].headers

@app.get("/read")
async def read():
    df = DataService.read_csv('data.csv')
    return {
        'df': df.to_dict()
    }

@app.get("/error", response_class=HTMLResponse)
async def simulate_error(request:Request):
    10 / 0
    return "err"



@app.get("/crash", response_class=HTMLResponse)
async def simulate_crash():
    i = 0
    def foo(i):
        i+=1
        return foo(i)
    foo(i)
    return f"{i}, crashing!"


@app.get("/timer", response_class=HTMLResponse)
async def timer2():
    i = 0
    while i<10:
        time.sleep(10)
        logger.warning(f"hello from timer {time.time()}")
        i+=1
# @app.get("/create")
# def create():
#     try:
#         df = DataService.generateData()
#         df.to_csv('data.csv')
#         r = {
#             'success': True
#         }
#     except Exception as e:
#         r = {
#             'success': False
#         }
    
#     return r


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


@app.post("/endpoint_ajax")
async def endpoint_ajax(request: Request):
    data = await request.json()
    # print(data)
    logger.debug(data)
    return JSONResponse(content=jsonable_encoder(data))
    # return Response(content=jsonable_encoder(data), media_type='application/json')
    # return data
    # return JSONResponse(content='Hello from server!') 




if __name__ == "__main__":
    # path_to_log_file = os.path.join('./logs', 'fastapi_TimedRotatingFileHandler.log')
    # logger = Logger(path_to_log_file)
    # logger = get_logger()
    # path_to_log_file = os.path.join('./logs', 'fastapi_TimedRotatingFileHandler.log')
    path_to_log_file = os.path.join('./logs', 'fastapi_FileHandler.log')
    log_config = Logger(path_to_log_file)
    # uvicorn.run("main:app", port=8888, reload=True, log_config=log_config.getConfig())
    uvicorn.run("main:app", port=8888, reload=True, log_config=log_config.getConfig())

    # uvicorn.run("main:app", port=8888, reload=True)

    # uvicorn.run("main:app", port=8888, reload=True, log_config='./log.ini')
    # uvicorn.run("main:app", port=8888, reload=True, log_config=log_config, access_log=True)
    # uvicorn.run("main:app", port=8888, reload=True, log_config=log_config)
    
    # uvicorn.run("main:app", port=8888, reload=True)