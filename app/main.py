from fastapi import FastAPI
from pydantic import BaseModel
from app.model import validate_action

app = FastAPI(title="Nudos AI – LazosTech")

class RecyclingInput(BaseModel):
    machine_id: str
    material: str
    weight_grams: float

@app.post("/ingest/recycling")
def ingest_recycling(data: RecyclingInput):
    validation = validate_action(data.weight_grams)

    tokens = round(data.weight_grams / 100, 2)

    return {
        "validated": validation["validated"],
        "confidence": validation["confidence"],
        "tokens_issued": tokens
    }
