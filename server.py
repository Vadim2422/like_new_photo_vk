import uvicorn
from threading import Thread


def run():
    uvicorn.run("main:app", host='0.0.0.0', port=8080)


def keep_alive():
    f = Thread(target=run)
    f.start()
