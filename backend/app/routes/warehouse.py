from fastapi import APIRouter,HTTPException
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

    existing_warehouse = db.query(Warehouse).filter(
        Warehouse.name == warehouse.name
    ).first()

    if existing_warehouse:
        raise HTTPException(
            status_code=400,
            detail="Warehouse already exists"
        )

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

@router.put("/{warehouse_id}", response_model=WarehouseResponse)
def update_warehouse(
    warehouse_id:int,
    warehouse_data : WarehouseCreate):

    db = SessionLocal()

    warehouse = db.query(Warehouse).filter(
        Warehouse.id == warehouse_id
    ).first()

    if not warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found")

    for key, value in warehouse_data.dict().items():
        setattr(warehouse, key, value)

    db.commit()
    db.refresh(warehouse)

    return warehouse

@router.delete("/{warehouse_id}")
def delete_warehouse(warehouse_id:int):

    db = SessionLocal()

    warehouse = db.query(Warehouse).filter(
        Warehouse.id == warehouse_id
    ).first()

    if not warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found")

    db.delete(warehouse)
    db.commit()

    return {"detail": "Warehouse deleted successfully"}
