import pandas as pd

from app.database import SessionLocal

from app.models.warehouse import Warehouse
from app.models.shipments import Shipment   
from app.models.inventory import Inventory

def load_shipments_csv(file_path:str):
    db = SessionLocal()
    
    try:
        df = pd.read_csv(file_path)

        for _,row in df.iterrows():
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

                cost=row[
                    "cost"
                ],

                distance_km=row[
                    "distance_km"
                ]
            )

            db.add(shipment)

        db.commit()

        return {
            "message": "Shipments CSV loaded successfully"
        }

    finally:
        db.close()

def load_inventory_csv(file_path:str):

    db = SessionLocal()
    try:
        df = pd.read_csv(file_path)
        
        for _,row in df.iterrows():
            inventory = Inventory(
                warehouse_id = row["warehouse_id"],
                product_name = row["product_name"],
                quantity = row["quantity"]
)
            db.add(inventory)
        db.commit()
        return {
            "message": "Inventory CSV loaded successfully"
        }
    finally:
        db.close()

def load_warehouses_csv(file_path:str):

    db = SessionLocal()
    try:
        df = pd.read_csv(file_path)

        for _,row in df.iterrows():
            warehouse = Warehouse(
                name=row["name"],
                city=row["city"],
                capacity=row["capacity"]
            )
            db.add(warehouse)
        db.commit()
        return {
            "message": "Warehouses CSV loaded successfully"
        }
    finally:       
        db.close()  