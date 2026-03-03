from fastapi import APIRouter
from datetime import datetime
from app.db.database import engine

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

@router.get("/db-test")
def db_test():
    try:
        with engine.connect() as connection:
            return {"database": "connected"}
    except Exception as e:
        return {"error": str(e)}