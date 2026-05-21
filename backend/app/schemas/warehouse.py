from pydantic import BaseModel

class WarehouseBase(BaseModel):
    name: str
    city: str
    capacity: int

    class Config:
        from_attributes = True