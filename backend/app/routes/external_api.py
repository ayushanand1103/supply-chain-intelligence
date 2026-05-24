from fastapi import APIRouter

from app.integration.external_api import (
    get_weather,get_coordinates,get_route_data
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

@router.get("/")
def geolocation(city: str):

    return get_coordinates(city)

@router.get("/route")
def route(

    source_lat: float,
    source_lon: float,

    destination_lat: float,
    destination_lon: float
):

    return get_route_data(

        source_lat,
        source_lon,

        destination_lat,
        destination_lon
    )