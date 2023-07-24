import aiohttp
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("BOT_API_KEY")

async def main():
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.get(f"https://api.telegram.org/bot{API_KEY}/getUpdates") as response:
                json = await response.json()
                print("JSON:", json)
                for elem in json["result"]:
                    print("TEXT:", f'"{elem["message"]["text"]}"')
                await asyncio.sleep(5) 
                os.system("CLS")


if __name__ == "__main__":
    asyncio.run(main())            
