from typing import Union

from fastapi import FastAPI
import uvicorn

from DataService import DataService

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/read")
def read():
    df = DataService.read_csv('data.csv')
    return {
        'df': df.to_dict()
    }

@app.get("/create")
def create():
    try:
        df = DataService.generateData()
        df.to_csv('data.csv')
        r = {
            'success': True
        }
    except Exception as e:
        r = {
            'success': False
        }
    
    return r


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)