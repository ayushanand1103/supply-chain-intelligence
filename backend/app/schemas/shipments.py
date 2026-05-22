from pydantic import BaseModel

class ShipmentCreate(BaseModel):
    source_warehouse_id: int
    destination_warehouse_id: int

    status: str
    delay_hours: int


class ShipmentResponse(ShipmentCreate):

    id: int

    class Config:
        from_attributes = True
