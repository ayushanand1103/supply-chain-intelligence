from pydantic import BaseModel


class WarehouseCreate(BaseModel):

    name: str

    city: str

    capacity: int


class WarehouseResponse(WarehouseCreate):

    id: int

    latitude: float

    longitude: float

    class Config:
        from_attributes = True