from fastapi import APIRouter

from app.integration.external_api import (
    get_weather
)

router = APIRouter(
    prefix="/external",
    tags=["external-api"]
)


@router.get("/weather")
def weather(
    latitude: float,
    longitude: float
):

    return get_weather(
        latitude,
        longitude
    )