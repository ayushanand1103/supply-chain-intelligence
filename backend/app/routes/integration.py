from fastapi import APIRouter , UploadFile, File
import shutil 

from app.integration.csv_loader import load_inventory_csv,load_warehouses_csv,load_shipments_csv

router = APIRouter(
    prefix="/integration",
    tags=["integration"]
)

@router.post("/upload-shipments")
def upload_shipments_csv(
    file: UploadFile = File(...)
):

    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    return load_shipments_csv(file_path)

@router.post("/upload-inventory")
def upload_inventory_csv(
    file: UploadFile = File(...)
):

    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    return load_inventory_csv(file_path)

@router.post("/upload-warehouses")
def upload_warehouses_csv(
    file: UploadFile = File(...)
):

    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    return load_warehouses_csv(file_path)

