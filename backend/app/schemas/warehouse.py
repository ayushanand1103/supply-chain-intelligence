from pydantic import BaseModel

class WarehouseCreate(BaseModel):
    name: str
    city: str
    capacity: int

    class Config:
        from_attributes = True

class WarehouseResponse(WarehouseCreate):
    id: int

    class Config:
        from_attributes = True