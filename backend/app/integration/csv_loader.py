import pandas as pd

from app.database import SessionLocal

from app.models.warehouse import Warehouse
from app.models.shipments import Shipment   
from app.models.inventory import Inventory
from app.integration.external_api import get_coordinates
from app.integration.external_api import get_route_data

def load_shipments_csv(file_path: str):

    db = SessionLocal()

    try:

        df = pd.read_csv(file_path)

        for _, row in df.iterrows():

            # =====================================
            # GET SOURCE WAREHOUSE
            # =====================================

            source_warehouse = db.query(Warehouse).filter(
                Warehouse.id == row["source_warehouse_id"]
            ).first()

            # =====================================
            # GET DESTINATION WAREHOUSE
            # =====================================

            destination_warehouse = db.query(Warehouse).filter(
                Warehouse.id == row["destination_warehouse_id"]
            ).first()

            if not source_warehouse or not destination_warehouse:
                continue

            # =====================================
            # ROUTE DATA
            # =====================================

            route_data = get_route_data(

                source_warehouse.latitude,
                source_warehouse.longitude,

                destination_warehouse.latitude,
                destination_warehouse.longitude
            )

            distance_km = route_data["distance_km"]

            estimated_time_hours = round(

                route_data["estimated_time_minutes"] / 60,

                2
            )

            # =====================================
            # AUTO COST
            # =====================================

            estimated_cost = round(
                distance_km * 8,
                2
            )

            # =====================================
            # CREATE SHIPMENT
            # =====================================

            shipment = Shipment(

                source_warehouse_id=row[
                    "source_warehouse_id"
                ],

                destination_warehouse_id=row[
                    "destination_warehouse_id"
                ],

                product_name=row[
                    "product_name"
                ],

                quantity=row[
                    "quantity"
                ],

                shipment_type=row[
                    "shipment_type"
                ],

                status=row[
                    "status"
                ],

                delay_hours=row[
                    "delay_hours"
                ],

                cost=estimated_cost,

                distance_km=distance_km,

                estimated_time_hours=
                estimated_time_hours
            )

            db.add(shipment)

        db.commit()

        return {
            "message": "Shipments CSV loaded successfully"
        }

    finally:
        db.close()

def load_inventory_csv(file_path: str):

    db = SessionLocal()

    try:

        df = pd.read_csv(file_path)

        for _, row in df.iterrows():

            inventory = Inventory(

                warehouse_id=row["warehouse_id"],

                product_name=row["product_name"],

                quantity=row["quantity"]
            )

            db.add(inventory)

        db.commit()

        return {
            "message":
            "Inventory CSV loaded successfully"
        }

    finally:
        db.close()

def load_warehouses_csv(file_path: str):

    db = SessionLocal()

    try:

        df = pd.read_csv(file_path)

        for _, row in df.iterrows():

            # ==============================
            # GET COORDINATES
            # ==============================

            location_data = get_coordinates(
                row["city"]
            )

            latitude = float(
                location_data["latitude"]
            )

            longitude = float(
                location_data["longitude"]
            )

            # ==============================
            # CREATE WAREHOUSE
            # ==============================

            warehouse = Warehouse(

                name=row["name"],

                city=row["city"],

                capacity=row["capacity"],

                latitude=latitude,

                longitude=longitude
            )

            db.add(warehouse)

        db.commit()

        return {
            "message":
            "Warehouses CSV loaded successfully"
        }

    finally:
        db.close()