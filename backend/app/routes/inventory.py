from fastapi import APIRouter, Depends, HTTPException

from app.database import SessionLocal
from app.models.inventory import Inventory
from app.schemas.inventory import InventoryCreate, InventoryResponse

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"]
)

@router.post("/", response_model=InventoryResponse)
def create_inventory(data: InventoryCreate):

    db = SessionLocal()

    try:

        inventory = Inventory(
            warehouse_id=data.warehouse_id,
            product_name=data.product_name,
            quantity=data.quantity
        )

        db.add(inventory)

        db.commit()

        db.refresh(inventory)

        return inventory

    finally:
        db.close()

@router.get("/", response_model=list[InventoryResponse])
def get_inventory():

    db = SessionLocal()

    try:

        inventory = db.query(Inventory).all()

        return inventory

    finally:
        db.close()


@router.get("/{warehouse_id}")
def get_inventory_by_warehouse(warehouse_id: int):

    db = SessionLocal()

    try:

        inventory = db.query(Inventory).filter(
            Inventory.warehouse_id == warehouse_id
        ).all()

        return inventory

    finally:
        db.close()

        

@router.put("/update-stock")
def update_stock(
    warehouse_id: int,
    product_name: str,
    quantity_change: int
):

    db = SessionLocal()

    try:

        inventory = db.query(Inventory).filter(
            Inventory.warehouse_id == warehouse_id,
            Inventory.product_name == product_name
        ).first()

        if not inventory:

            raise HTTPException(
                status_code=404,
                detail="Inventory item not found"
            )

        inventory.quantity += quantity_change

        if inventory.quantity < 0:

            raise HTTPException(
                status_code=400,
                detail="Insufficient stock"
            )

        db.commit()

        db.refresh(inventory)

        return {
            "message": "Stock updated successfully",
            "updated_quantity": inventory.quantity
        }

    finally:
        db.close()
