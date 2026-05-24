from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey
)

from datetime import datetime

from app.database import Base


class Shipment(Base):

    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, index=True)

    source_warehouse_id = Column(
        Integer,
        ForeignKey("warehouses.id"),
        nullable=False
    )

    destination_warehouse_id = Column(
        Integer,
        ForeignKey("warehouses.id"),
        nullable=False
    )

    product_name = Column(
        String,
        nullable=False
    )

    quantity = Column(
        Integer,
        nullable=False
    )

    shipment_type = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        nullable=False
    )

    delay_hours = Column(
        Integer,
        default=0
    )

    cost = Column(
        Float,
        default=0
    )

    # AUTO GENERATED FROM OSRM
    distance_km = Column(
        Float,
        default=0
    )

    # AUTO GENERATED FROM OSRM
    estimated_time_hours = Column(
        Float,
        default=0
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )