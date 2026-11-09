import asyncio
import os
from dataclasses import dataclass

import aiohttp
from dotenv import load_dotenv

load_dotenv()

API_KEY: str = os.getenv("API_KEY")
BASE_URL: str = "https://api.openweathermap.org/data/2.5/weather"


@dataclass
class Weather:
    city: str
    temp: float
    description: str
    humidity: int


async def fetch_wether(
        session : aiohttp.ClientSession,
        city: str,
        units: str = "metric",
        lang: str = "ru"
) -> Weather | None:
    params: dict = {
        "q": city,
        "appid": API_KEY,
        "units": units,
        "lang": lang
    }

    try:
        async with session.get(BASE_URL, params=params) as response:
            if response.status == 401:
                print("API key error")
                return None
            if response.status == 404:
                print("City no found")
                return None
            response.raise_for_status()

            data = await response.json()
    except aiohttp.ClientError as e:
        print(e)
        return None

    return Weather(
        city=city,
        temp=data["main"]["temp"],
        description=data["weather"][0]["description"],
        humidity=data["main"]["humidity"]
    )
