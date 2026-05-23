from fastapi import APIRouter

from app.database import SessionLocal
from app.models.warehouse import Warehouse
from app.models.shipments import Shipment


router = APIRouter(
    prefix="/analytics",
    tags=["analytics"]
)


# =========================================
# OVERVIEW ANALYTICS
# =========================================

@router.get("/overview")
def get_overview():

    db = SessionLocal()

    try:

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

    finally:
        db.close()


# =========================================
# DELAYED SHIPMENTS
# =========================================

@router.get("/delays")
def get_delayed_shipments():

    db = SessionLocal()

    try:

        delayed_shipments = db.query(Shipment).filter(
            Shipment.delay_hours > 0
        ).all()

        return delayed_shipments

    finally:
        db.close()


# =========================================
# HIGH RISK SHIPMENTS
# =========================================

@router.get("/high-risk")
def get_high_risk_shipments():

    db = SessionLocal()

    try:

        high_risk_shipments = db.query(Shipment).filter(
            Shipment.delay_hours >= 24
        ).all()

        return {
            "high_risk_shipments": high_risk_shipments,
            "count": len(high_risk_shipments)
        }

    finally:
        db.close()


# =========================================
# SHIPMENT STATUS SUMMARY
# =========================================

@router.get("/status-summary")
def shipment_status_summary():

    db = SessionLocal()

    try:

        shipments = db.query(Shipment).all()

        summary = {}

        for shipment in shipments:

            status = shipment.status

            if status not in summary:
                summary[status] = 0

            summary[status] += 1

        return summary

    finally:
        db.close()


# =========================================
# BOTTLENECK DETECTION
# =========================================

@router.get("/bottlenecks")
def detect_bottlenecks():

    db = SessionLocal()

    try:

        shipments = db.query(Shipment).all()

        warehouse_delays = {}

        for shipment in shipments:

            warehouse_id = shipment.source_warehouse_id

            if warehouse_id not in warehouse_delays:

                warehouse_delays[warehouse_id] = 0

            warehouse_delays[warehouse_id] += shipment.delay_hours

        return warehouse_delays

    finally:
        db.close()


# =========================================
# RISK SCORE ANALYTICS
# =========================================

@router.get("/risk-scores")
def shipment_risk_scores():

    db = SessionLocal()

    try:

        shipments = db.query(Shipment).all()

        risk_analysis = []

        for shipment in shipments:

            if shipment.delay_hours == 0:
                risk = "Low"

            elif shipment.delay_hours < 12:
                risk = "Medium"

            elif shipment.delay_hours < 24:
                risk = "High"

            else:
                risk = "Critical"

            risk_analysis.append({
                "shipment_id": shipment.id,
                "delay_hours": shipment.delay_hours,
                "risk_level": risk
            })

        return risk_analysis

    finally:
        db.close()


# =========================================
# COST ANALYTICS
# =========================================

@router.get("/cost-analysis")
def cost_analysis():

    db = SessionLocal()

    try:

        shipments = db.query(Shipment).all()

        total_cost = sum(
            shipment.cost for shipment in shipments
        )

        average_cost = (
            total_cost / len(shipments)
            if shipments else 0
        )

        return {
            "total_transportation_cost": total_cost,
            "average_shipment_cost": round(average_cost, 2)
        }

    finally:
        db.close()

@router.get("/distance-analysis")
def distance_analysis():

    db = SessionLocal()

    try:

        shipments = db.query(Shipment).all()

        total_distance = sum(
            shipment.distance_km for shipment in shipments
        )

        average_distance = (
            total_distance / len(shipments)
            if shipments else 0
        )

        return {
            "total_distance_covered": total_distance,
            "average_distance": round(average_distance, 2)
        }

    finally:
        db.close()


    




        
