from datetime import datetime
from typing import Dict
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root() -> str:
    return "New Life Bank"

@app.get("/health/")
def alive() -> Dict[str, datetime]:
    return {"timestamp": datetime.now()}