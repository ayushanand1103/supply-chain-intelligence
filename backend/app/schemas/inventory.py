from pydantic import BaseModel

class InventoryCreate(BaseModel):

    warehouse_id: int
    product_name: str
    quantity: int


class InventoryResponse(InventoryCreate):

    id: int

    class Config:
        from_attributes = True