import requests
from langchain_core.tools import tool

from src.utils.env import env


@tool
def get_word_length(word: str) -> int:
    """Returns the length of a word."""
    # needs doc string to work
    return len(word)


@tool
def get_current_weather() -> dict:
    """Returns the current weather"""
    city = "macapa"
    state_code = "AP"
    country_code = "BR"

    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state_code},{country_code}&limit={1}&appid={env.OPEN_WEATHER_API_KEY}"

    _res = requests.get(url).json()

    lat = _res[0]['lat']
    lon = _res[0]['lon']

    forecast_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={env.OPEN_WEATHER_API_KEY}&units=metric"

    forecast = requests.get(forecast_url).json()

    return {
        "city": forecast["name"],
        "temperature": forecast["main"]["temp"],
        "feels_like": forecast["main"]["feels_like"],
        "humidity": forecast["main"]["humidity"],
        "weather": forecast["weather"][0]["description"],
    }


@tool
def get_todos():
    """Returns the user upcoming todos"""

    return {
        "todos": [
            {
                "title": "Buy groceries",
                "dueDate": "2024-05-01",
            },
            {
                "title": "Make food",
                "dueDate": None
            }
        ]
    }


tools = [get_todos, get_word_length, get_current_weather]
