from fastapi import APIRouter, HTTPException

from app.database import SessionLocal

from app.models.shipments import Shipment
from app.models.inventory import Inventory

from app.schemas.shipments import (
    ShipmentCreate,
    ShipmentResponse
)

router = APIRouter(
    prefix="/shipments",
    tags=["shipments"]
)


# =========================================
# CREATE SHIPMENT
# =========================================

@router.post("/", response_model=ShipmentResponse)
def create_shipment(shipment: ShipmentCreate):

    db = SessionLocal()

    try:

        # =====================================
        # CHECK SOURCE INVENTORY
        # =====================================

        source_inventory = db.query(Inventory).filter(
            Inventory.warehouse_id ==
            shipment.source_warehouse_id,

            Inventory.product_name ==
            shipment.product_name
        ).first()

        if not source_inventory:

            raise HTTPException(
                status_code=404,
                detail="Product not found in source warehouse"
            )

        if source_inventory.quantity < shipment.quantity:

            raise HTTPException(
                status_code=400,
                detail="Not enough stock in source warehouse"
            )

        # =====================================
        # REDUCE SOURCE STOCK
        # =====================================

        source_inventory.quantity -= shipment.quantity

        # =====================================
        # DESTINATION INVENTORY
        # =====================================

        destination_inventory = db.query(Inventory).filter(
            Inventory.warehouse_id ==
            shipment.destination_warehouse_id,

            Inventory.product_name ==
            shipment.product_name
        ).first()

        # if product already exists in destination
        if destination_inventory:

            destination_inventory.quantity += shipment.quantity

        else:

            # create new inventory entry
            new_inventory = Inventory(
                warehouse_id=shipment.destination_warehouse_id,
                product_name=shipment.product_name,
                quantity=shipment.quantity
            )

            db.add(new_inventory)

        # =====================================
        # CREATE SHIPMENT
        # =====================================

        new_shipment = Shipment(
            source_warehouse_id=shipment.source_warehouse_id,
            destination_warehouse_id=shipment.destination_warehouse_id,
            product_name=shipment.product_name,
            quantity=shipment.quantity,
            shipment_type=shipment.shipment_type,
            status=shipment.status,
            delay_hours=shipment.delay_hours,
            cost=shipment.cost,
            distance_km=shipment.distance_km
        )

        db.add(new_shipment)

        db.commit()

        db.refresh(new_shipment)

        return new_shipment

    finally:
        db.close()


# =========================================
# GET ALL SHIPMENTS
# =========================================

@router.get("/", response_model=list[ShipmentResponse])
def get_shipments():

    db = SessionLocal()

    try:

        shipments = db.query(Shipment).all()

        return shipments

    finally:
        db.close()


# =========================================
# GET SHIPMENT BY ID
# =========================================

@router.get("/{shipment_id}", response_model=ShipmentResponse)
def get_shipment_by_id(shipment_id: int):

    db = SessionLocal()

    try:

        shipment = db.query(Shipment).filter(
            Shipment.id == shipment_id
        ).first()

        if not shipment:

            raise HTTPException(
                status_code=404,
                detail="Shipment not found"
            )

        return shipment

    finally:
        db.close()


# =========================================
# DELETE SHIPMENT
# =========================================

@router.delete("/{shipment_id}")
def delete_shipment(shipment_id: int):

    db = SessionLocal()

    try:

        shipment = db.query(Shipment).filter(
            Shipment.id == shipment_id
        ).first()

        if not shipment:

            raise HTTPException(
                status_code=404,
                detail="Shipment not found"
            )

        db.delete(shipment)

        db.commit()

        return {
            "message": "Shipment deleted successfully"
        }

    finally:
        db.close()