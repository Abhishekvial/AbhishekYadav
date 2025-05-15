from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from gnn_model import predict_risk

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VulnerabilityInput(BaseModel):
    description: str

@app.post("/analyze")
def analyze_vulnerability(data: VulnerabilityInput):
    result = predict_risk(data.description)
    return result
