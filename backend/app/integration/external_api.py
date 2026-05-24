import requests


def get_weather():

    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=28.61"
        "&longitude=77.23"
        "&current_weather=true"
    )

    response = requests.get(url)

    data = response.json()

    current = data["current_weather"]

    return {

        "temperature": current["temperature"],

        "wind_speed": current["windspeed"],

        "weather_code": current["weathercode"]
    }