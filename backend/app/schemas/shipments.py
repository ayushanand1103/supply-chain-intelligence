from pydantic import BaseModel


class ShipmentCreate(BaseModel):

    source_warehouse_id: int

    destination_warehouse_id: int

    product_name: str

    quantity: int

    shipment_type: str

    status: str

    delay_hours: int

class ShipmentResponse(ShipmentCreate):

    id: int

    cost: float

    distance_km: float

    estimated_time_hours: float

    class Config:
        from_attributes = True