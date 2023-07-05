"""Weather aplication."""
import random
import os
import aiohttp
import asyncio
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

coordinates = [(47.2313500, 39.7232800), (55.7522, 37.6156), (43.5992, 39.7257), (44.5022,  34.1662)]

async def main():
    async with aiohttp.ClientSession() as session:
        number = 1
        for lat, lon in coordinates:
            async with session.get(
                    f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}") as response:
                json_data = await response.json()
                print(number, {"status": response.status, "city": json_data["name"], "tempature": round(int(json_data["main"]["temp"]) - 273.15, 2)})
                number += 1


if __name__ == "__main__":
    asyncio.run(main())
