from fastapi import APIRouter, HTTPException

from app.database import SessionLocal

from app.models.shipments import Shipment
from app.models.inventory import Inventory
from app.models.warehouse import Warehouse

from app.schemas.shipments import (
    ShipmentCreate,
    ShipmentResponse
)

from app.integration.external_api import (
    get_route_data
)
from app.services.eta_service import ETAService

eta_service = ETAService()

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
        # SOURCE WAREHOUSE
        # =====================================

        source_warehouse = db.query(Warehouse).filter(
            Warehouse.id ==
            shipment.source_warehouse_id
        ).first()

        if not source_warehouse:

            raise HTTPException(
                status_code=404,
                detail="Source warehouse not found"
            )

        # =====================================
        # DESTINATION WAREHOUSE
        # =====================================

        destination_warehouse = db.query(Warehouse).filter(
            Warehouse.id ==
            shipment.destination_warehouse_id
        ).first()

        if not destination_warehouse:

            raise HTTPException(
                status_code=404,
                detail="Destination warehouse not found"
            )

        # =====================================
        # ROUTE CALCULATION
        # =====================================

        route_data = get_route_data(

            source_warehouse.latitude,
            source_warehouse.longitude,

            destination_warehouse.latitude,
            destination_warehouse.longitude
        )

        distance_km = route_data["distance_km"]

        eta_result = eta_service.get_eta(
                            source_id=shipment.source_warehouse_id,
                            dest_id=shipment.destination_warehouse_id,
                            distance_km=distance_km,
                            duration_hours=route_data["estimated_time_minutes"] / 60)

        estimated_time_hours = eta_result["final_eta_hours"]

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
                detail="Not enough stock available"
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

        if destination_inventory:

            destination_inventory.quantity += shipment.quantity

        else:

            new_inventory = Inventory(

                warehouse_id=
                shipment.destination_warehouse_id,

                product_name=
                shipment.product_name,

                quantity=
                shipment.quantity
            )

            db.add(new_inventory)

        # =====================================
        # AUTO COST CALCULATION
        # =====================================

        estimated_cost = round(
            distance_km * 8,
            2
        )

        # =====================================
        # CREATE SHIPMENT
        # =====================================

        new_shipment = Shipment(

            source_warehouse_id=
            shipment.source_warehouse_id,

            destination_warehouse_id=
            shipment.destination_warehouse_id,

            product_name=
            shipment.product_name,

            quantity=
            shipment.quantity,

            shipment_type=
            shipment.shipment_type,

            status=
            shipment.status,

            delay_hours=
            shipment.delay_hours,

            cost=
            estimated_cost,

            distance_km=
            distance_km,

            estimated_time_hours=
            estimated_time_hours
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