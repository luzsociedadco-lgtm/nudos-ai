from fastapi import FastAPI
from app.model import analyze_event

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Nudos AI running"}

@app.post("/analyze")
def analyze(data: dict):
    return analyze_event(data)
