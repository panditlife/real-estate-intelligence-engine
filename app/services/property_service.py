from sqlalchemy.orm import Session
from app.db.models import Property

def create_property(db: Session, title: str, location: str, price: float, rent: float):
    property_obj = Property(
        title=title,
        location=location,
        price=price,
        rent=rent
    )
    db.add(property_obj)
    db.commit()
    db.refresh(property_obj)
    return property_obj

def get_all_properties(db: Session):
    return db.query(Property).all()