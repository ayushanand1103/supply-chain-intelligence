from pydantic import BaseModel
from datetime import datetime


class ShipmentCreate(BaseModel):

    source_warehouse_id: int
    destination_warehouse_id: int

    status: str

    delay_hours: int = 0

    cost: float = 0
    distance_km: float = 0



class ShipmentResponse(ShipmentCreate):

    id: int

    class Config:
        from_attributes = True
