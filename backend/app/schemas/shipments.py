from pydantic import BaseModel


class ShipmentCreate(BaseModel):

    source_warehouse_id: int

    destination_warehouse_id: int

    product_name: str

    quantity: int

    shipment_type: str

    status: str

    delay_hours: int

    cost: float

    distance_km: float


class ShipmentResponse(ShipmentCreate):

    id: int

    class Config:
        from_attributes = True