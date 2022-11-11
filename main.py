from fastapi import FastAPI
import subprocess

app = FastAPI()


@app.get("/")
async def root():
    stream_pipe = subprocess.call('../stream.sh')
    return {"message": stream_pipe}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
