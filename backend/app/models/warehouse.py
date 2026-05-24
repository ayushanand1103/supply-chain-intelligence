from sqlalchemy import (
    Column,
    Integer,
    String,
    Float
)

from sqlalchemy.orm import relationship

from app.database import Base


class Warehouse(Base):

    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    city = Column(String, nullable=False)

    capacity = Column(Integer, nullable=False)

    latitude = Column(Float, nullable=False)

    longitude = Column(Float, nullable=False)

    outgoing_shipments = relationship(
        "Shipment",
        foreign_keys="Shipment.source_warehouse_id"
    )

    incoming_shipments = relationship(
        "Shipment",
        foreign_keys="Shipment.destination_warehouse_id"
    )