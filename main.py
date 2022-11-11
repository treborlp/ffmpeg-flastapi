from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
async def root():
    stream = os.popen('ls -l')
    output = stream.read()
    return {"message": output}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
