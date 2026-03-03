from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Real Estate Intelligence Engine")

@app.get("/")
def root():
    return {"message": "Real Estate Intelligence Engine is running"}

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.utcnow()
    }