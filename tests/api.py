from os import system
from time import sleep
from fastapi import FastAPI


app = FastAPI()


@app.get("/", status_code=200)
async def make_get():
    return {"message": "GET"}


@app.post("/", status_code=201)
async def meke_post():
    return {"message": "POST"}


@app.put("/", status_code=200)
async def make_put():
    return {"message": "PUT"}


@app.delete("/", status_code=200)
async def make_delete():
    return {"message": "DELETE"}


def start():
    system('nohup uvicorn tests.api:app --host 0.0.0.0 --reload &')
    sleep(5)


def stop():
    system('nohup pkill uvicorn &')