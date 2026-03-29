import requests


def get_weather(latitude: float, longitude: float) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ["temperature_2m", "wind_speed_10m", "weather_code"],
        "temperature_unit": "celsius",
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def main():
    # Coordinates for New York City
    lat, lon = 40.7128, -74.0060

    print(f"Fetching weather for coordinates ({lat}, {lon})...")
    data = get_weather(lat, lon)

    current = data["current"]
    print(f"Temperature : {current['temperature_2m']} °C")
    print(f"Wind speed  : {current['wind_speed_10m']} km/h")
    print(f"Weather code: {current['weather_code']}")


if __name__ == "__main__":
    main()
