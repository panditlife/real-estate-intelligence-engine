from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Real Estate Intelligence Engine is running"}

@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.utcnow()
    }