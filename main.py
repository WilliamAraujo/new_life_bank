import uvicorn
from typing import Dict
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def root() -> str:
    return "Welcome to New Life Bank"

@app.get("/health")
def alive() -> Dict[str, datetime]:
    return {"timestamp": datetime.now()}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
