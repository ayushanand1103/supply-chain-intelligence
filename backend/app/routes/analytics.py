from fastapi import APIRouter

from app.database import SessionLocal
from app.models.warehouse import Warehouse
from app.models.shipments import Shipment

router = APIRouter(
    prefix="/analytics",
    tags=["analytics"]
)

@router.get("/overview")
def get_overview():

    db = SessionLocal()

    total_warehouses = db.query(Warehouse).count()

    total_shipments = db.query(Shipment).count()

    delayed_shipments = db.query(Shipment).filter(
        Shipment.delay_hours > 0
    ).count()

    shipments = db.query(Shipment).all()

    if shipments:

        average_delay = sum(
            shipment.delay_hours for shipment in shipments
        ) / len(shipments)

    else:
        average_delay = 0

    return {
        "total_warehouses": total_warehouses,
        "total_shipments": total_shipments,
        "delayed_shipments": delayed_shipments,
        "average_delay_hours": round(average_delay, 2)
    }