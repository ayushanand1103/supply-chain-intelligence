import requests


def get_weather(
    latitude: float,
    longitude: float
):

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current_weather=true"
    )

    response = requests.get(url)

    data = response.json()

    current = data["current_weather"]

    return {

        "latitude": latitude,

        "longitude": longitude,

        "temperature": current["temperature"],

        "wind_speed": current["windspeed"],

        "wind_direction": current["winddirection"],

        "weather_code": current["weathercode"],

        "time": current["time"]
    }


def get_coordinates(city: str):

    url = (
        "https://nominatim.openstreetmap.org/search"
        f"?q={city}"
        "&format=json"
        "&limit=1"
    )

    headers = {
        "User-Agent": "supply-chain-intelligence"
    }

    response = requests.get(
        url,
        headers=headers
    )

    data = response.json()

    if not data:

        return {
            "error": "Location not found"
        }

    location = data[0]

    return {

        "city": city,

        "latitude": location["lat"],

        "longitude": location["lon"],

        "display_name": location["display_name"]
    }




def get_route_data(

    source_lat: float,
    source_lon: float,

    destination_lat: float,
    destination_lon: float
):

    url = (

        "http://router.project-osrm.org/route/v1/driving/"

        f"{source_lon},{source_lat};"

        f"{destination_lon},{destination_lat}"

        "?overview=false"
    )

    response = requests.get(url)

    data = response.json()

    if not data.get("routes"):

        return {
            "error": "Route not found"
        }

    route = data["routes"][0]

    return {

        "distance_km": round(
            route["distance"] / 1000,
            2
        ),

        "estimated_time_minutes": round(
            route["duration"] / 60,
            2
        )
    }