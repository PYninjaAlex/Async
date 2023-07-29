import aiohttp
import asyncio
from dotenv import load_dotenv
from pprint import pprint
from TelegramRequestData import TelegramRequestData
import os

load_dotenv()

API_KEY = os.getenv("BOT_API_KEY")
API_URL = f"https://api.telegram.org/bot{API_KEY}"

async def get_updates(session):
    async with session.get(f"{API_URL}/getUpdates") as updates:
        updates_json = await updates.json()
        pprint(updates_json)
        return updates_json

async def send_message(session, chat_id, text):
    async with session.get(f"{API_URL}/sendMessage?chat_id={chat_id}&text={text}") as response:  
        json = await response.json()
        pprint(json)

async def main():
    async with aiohttp.ClientSession() as session:
        result = TelegramRequestData(json=await get_updates(session))
        print(result.chat_id)
        print(result.first_name)
        print(result.is_bot)
        text = input()
        await send_message(session, result.chat_id, text)
        

if __name__ == "__main__":
    asyncio.run(main())            

