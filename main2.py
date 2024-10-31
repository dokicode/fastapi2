import uvicorn
from fastapi import FastAPI
import httpx

app = FastAPI()

client: httpx.AsyncClient = None

@app.on_event('startup')
async def startup():
    print('startup')
    global client
    client = httpx.AsyncClient(timeout=None, follow_redirects=True)

@app.on_event('shutdown')
async def shutdown():
    print('shutdown')
    await client.aclose()


@app.get('/')
async def root():
    res = await client.get("https://httpbin.org/get")
    # res = await client.get("http://irkutskles.ru")
    return res.text


if __name__ == "__main__":
    uvicorn.run(app="main2:app", port=8888, reload=True)