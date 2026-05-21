from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.warehouse import Warehouse
from app.schemas.warehouse import WarehouseBase

router = APIRouter(
    prefix="/warehouses",
    tags=["warehouses"]
)

@router.post("/", response_model=WarehouseBase)
def create_warehouse(warehouse: WarehouseBase):

    db = SessionLocal()

    db_warehouse = Warehouse(
        name=warehouse.name,
        city=warehouse.city,
        capacity=warehouse.capacity
    )

    db.add(db_warehouse)
    db.commit()
    db.refresh(db_warehouse)

    return db_warehouse