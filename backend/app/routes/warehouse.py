from fastapi import APIRouter,HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.warehouse import Warehouse
from app.schemas.warehouse import WarehouseCreate, WarehouseResponse

from app.integration.external_api import get_coordinates

router = APIRouter(
    prefix="/warehouses",
    tags=["warehouses"]
)



# =========================================
# CREATE WAREHOUSE
# =========================================

@router.post("/", response_model=WarehouseResponse)
def create_warehouse(
    warehouse: WarehouseCreate
):

    db = SessionLocal()

    try:

        # =====================================
        # GET COORDINATES
        # =====================================

        location_data = get_coordinates(
            warehouse.city
        )

        if "error" in location_data:

            raise HTTPException(
                status_code=400,
                detail="Could not fetch coordinates"
            )

        latitude = float(
            location_data["latitude"]
        )

        longitude = float(
            location_data["longitude"]
        )

        # =====================================
        # CREATE WAREHOUSE
        # =====================================

        new_warehouse = Warehouse(

            name=warehouse.name,

            city=warehouse.city,

            capacity=warehouse.capacity,

            latitude=latitude,

            longitude=longitude
        )

        db.add(new_warehouse)

        db.commit()

        db.refresh(new_warehouse)

        return new_warehouse

    finally:
        db.close()


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
