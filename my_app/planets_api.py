import asyncio
import time
import aiohttp
import os
from dotenv import load_dotenv
from random import randint

load_dotenv()

API_KEY = os.getenv("NASA_API_KEY")
random_dates = []

for _ in range(20):
    random_dates.append(f"{randint(2000, 2022)}-{randint(1, 12)}-{randint(1, 28)}")


async def main(api_key, dates):
    pictures = []
    async with aiohttp.ClientSession() as session:
        for i, date in enumerate(dates):
            async with session.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}") as response:
                json_data = await response.json()
                pictures.append({"num": i+1, "status": response.status,
                                 'title': json_data["title"],
                                 'url': json_data["url"],
                                 'media_type': json_data["media_type"]
                                 })
    return pictures


res = asyncio.run(main(API_KEY, random_dates))
