import json
import pprint
from typing import Any
from fastapi import FastAPI, Request
from fastapi.middleware import Middleware
import httpx
import uvicorn
from contextlib import asynccontextmanager


pp = pprint.PrettyPrinter(indent=4)

class MyMiddleware:
    def __init__(self, app: FastAPI) -> None:
        self.app = app

    async def __call__(self, scope, receive, send):
        # message = await receive()
        # pp.pprint(message)
        
        # pp.pprint(scope)
        if scope["type"] == "http":
            scope["state"]["potato"] = "potato"
        print()
        print('Middleware')
        print()
        # pp.pprint(scope)
        return await self.app(scope, receive, send)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("start up!")
    async with httpx.AsyncClient(timeout=None) as client:
        yield {"client": client}
    print("shut down!")


app = FastAPI(lifespan=lifespan, middleware=[Middleware(MyMiddleware)])
app.state.potato = "Potato  "

@app.get("/")
async def root(request: Request):
    # res = await request.state.client.get("https://httpbin.org/get")
    res = await request['state']['client'].get("https://httpbin.org/get")
    return res.text

@app.get("/state")
async def state(request: Request):
    # if not hasattr(request.state, "foo"):
    #     print("I don't have a foo!!!")
    # if hasattr(request.state, "client"):
    #     print("I have a client!!!")
    # if hasattr(request.state, "potato"):
    #     print("I have a potato!!!")
    # request.state.foo = "foo"
    # return request.state.foo
    return request.app.state

@app.get("/server")
async def get_server_state():
    print(f"Server running", server.started)
    if server.started:
        answer = f"Server running"
    else:
        answer = f"Server isn't running"
    return answer


config = uvicorn.Config(app="lifespan:app", port=8888, reload=True)
server = uvicorn.Server(config=config)


if __name__ == "__main__":
    # print(dir(server))
    try:
        server.run()
    except Exception as e:
        print('Exception', e)
    print("##############################################")

    # uvi = server.run()
    # print(uvi)
    
    # uvicorn.run(app="lifespan:app", port=8888, reload=True)