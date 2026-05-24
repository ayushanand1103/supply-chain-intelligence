from fastapi import FastAPI

from app.database import engine, Base
from app.models.warehouse import Warehouse
from app.routes.warehouse import router as warehouse_router
from app.models.shipments import Shipment
from app.routes.shipments import router as shipment_router
from app.routes.analytics import router as analytics_router
from app.routes.inventory import router as inventory_router
from app.routes.integration import router as integration_router
from app.routes.external_api import router as external_api_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(warehouse_router)
app.include_router(shipment_router)
app.include_router(analytics_router)
app.include_router(inventory_router)
app.include_router(integration_router)
app.include_router(external_api_router)

@app.get("/", tags=["system"])
def home():
    return {"message": "Supply Chain Intelligence API"}

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)