from pydantic import BaseModel

class PropertyCreate(BaseModel):
    title: str
    location: str
    price: float
    rent: float

class PropertyResponse(BaseModel):
    id: int
    title: str
    location: str
    price: float
    rent: float

    class Config:
        from_attributes = True