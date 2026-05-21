from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.warehouse import Warehouse
from app.schemas.warehouse import WarehouseCreate, WarehouseResponse

router = APIRouter(
    prefix="/warehouses",
    tags=["warehouses"]
)

@router.post("/", response_model=WarehouseResponse)
def create_warehouse(warehouse: WarehouseCreate):
    
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


@router.get("/", response_model=list[WarehouseResponse])
def get_warehouses():
    
    db = SessionLocal()

    warehouses = db.query(Warehouse).all()

    return warehouses

@router.get("/{warehouse_id}", response_model=WarehouseResponse)
def get_warehouse_by_id(warehouse_id: int):

    db = SessionLocal()

    warehouse = db.query(Warehouse).filter(
        Warehouse.id == warehouse_id
    ).first()

    return warehouse
