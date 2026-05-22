from fastapi import APIRouter,HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.shipments import shimpment
from app.schemas.shipments import ShipmentCreate, ShipmentResponse

router = APIRouter(
    prefix="/shipments",
    tags=["shipments"]
)

@router.post("/",response_model = ShipmentResponse)
def create_shipment(shipment: ShipmentCreate):

    db = SessionLocal()

    db_shipment = shipment(
        source = shipment.source,
        destination = shipment.destination,
        status = shipment.status,
        delay_hours = shipment.delay_hours
    )

    db.add(db_shipment)
    db.commit()
    db.refresh(db_shipment)
    