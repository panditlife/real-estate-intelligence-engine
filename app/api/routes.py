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

from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.property_service import create_property, get_all_properties


from app.schemas.property import PropertyCreate, PropertyResponse
"""
@router.post("/properties")
def add_property(title: str, location: str, price: float, rent: float, db: Session = Depends(get_db)):
    return create_property(db, title, location, price, rent)

@router.get("/properties")
def list_properties(db: Session = Depends(get_db)):
    return get_all_properties(db)        
"""
@router.post("/properties", response_model=PropertyResponse)
def add_property(property: PropertyCreate, db: Session = Depends(get_db)):
    return create_property(
        db,
        title=property.title,
        location=property.location,
        price=property.price,
        rent=property.rent
    )

@router.get("/properties", response_model=list[PropertyResponse])
def list_properties(db: Session = Depends(get_db)):
    return get_all_properties(db)
