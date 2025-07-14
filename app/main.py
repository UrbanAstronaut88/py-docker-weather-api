import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable is not set")
        return

    city = "Paris"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        print(f"Weather in {city}: {description}, Temperature {temp}°C")

    except requests.exceptions.RequestException as e:
        print(f"Error getting weather: {e}")


if __name__ == "__main__":
    get_weather()
