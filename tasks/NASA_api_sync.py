import requests
from dotenv import load_dotenv
import os
import time
from random import randint

load_dotenv()

API_KEY = os.getenv("NASA_API_KEY")
random_dates = []

for _ in range(20):
    random_dates.append(f"{randint(2000, 2022)}-{randint(1, 12)}-{randint(1, 28)}")


def get_image_data(api_key, dates):
    for i, date in enumerate(dates):
        response = requests.get(
            f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}")
        json_data = response.json()
        print(i, {
            'title': json_data["title"],
            'url': json_data["url"],
            'media_type': json_data["media_type"]
        })


start_time = time.time()
get_image_data(API_KEY, random_dates)
end_time = time.time() - start_time

print(end_time, "seconds.")
