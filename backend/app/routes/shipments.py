from fastapi import APIRouter, HTTPException

from app.database import SessionLocal
from app.models.shipments import Shipment
from app.schemas.shipments import ShipmentCreate, ShipmentResponse

router = APIRouter(
    prefix="/shipments",
    tags=["shipments"]
)

@router.post("/", response_model=ShipmentResponse)
def create_shipment(shipment: ShipmentCreate):

    db = SessionLocal()

    db_shipment = Shipment(
        source_warehouse_id=shipment.source_warehouse_id,
        destination_warehouse_id=shipment.destination_warehouse_id,
        status=shipment.status,
        delay_hours=shipment.delay_hours
    )

    db.add(db_shipment)

    db.commit()

    db.refresh(db_shipment)

    return db_shipment

@router.get("/", response_model=list[ShipmentResponse])
def get_shipments():

    db = SessionLocal()

    shipments = db.query(Shipment).all()

    return shipments


@router.get("/{shipment_id}", response_model=ShipmentResponse)
def get_shipment_by_id(shipment_id: int):

    db = SessionLocal()

    shipment = db.query(Shipment).filter(
        Shipment.id == shipment_id
    ).first()

    return shipment


@router.put("/{shipment_id}", response_model=ShipmentResponse)
def update_shipment(
    shipment_id: int,
    shipment_data: ShipmentCreate
):

    db = SessionLocal()

    shipment = db.query(Shipment).filter(
        Shipment.id == shipment_id
    ).first()

    if not shipment:
        raise HTTPException(
            status_code=404,
            detail="Shipment not found"
        )

    shipment.source_warehouse_id = shipment_data.source_warehouse_id
    shipment.destination_warehouse_id = shipment_data.destination_warehouse_id
    shipment.status = shipment_data.status
    shipment.delay_hours = shipment_data.delay_hours

    db.commit()
    db.refresh(shipment)

    return shipment


@router.delete("/{shipment_id}")
def delete_shipment(shipment_id: int):

    db = SessionLocal()

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