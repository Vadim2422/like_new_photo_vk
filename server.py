import uvicorn
from threading import Thread

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def get():
    return 'get'


@app.head('/')
def head():
    return 'head'


def run():
    uvicorn.run("server:app", host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
