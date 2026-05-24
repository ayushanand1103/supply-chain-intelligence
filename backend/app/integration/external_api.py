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