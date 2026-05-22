from fastapi import FastAPI

from app.database import engine, Base
from app.models.warehouse import Warehouse
from app.routes.warehouse import router as warehouse_router
from app.models.shipments import Shipment
from app.routes.shipments import router as shipment_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(warehouse_router)
app.include_router(shipment_router)

@app.get("/", tags=["system"])
def home():
    return {"message": "Supply Chain Intelligence API"}