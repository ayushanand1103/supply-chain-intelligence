from pydantic import BaseModel

class ShipmentCreate(Basemodel):
    source: str
    destination: str
    status: str
    delay_hours: int

class ShipmentResponse(ShipmentCreate):

    id: int

    class Config:
        from_attributes = True
        