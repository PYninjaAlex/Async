import aiohttp
import asyncio
from dotenv import load_dotenv
from pprint import pprint
from dataclasses import dataclass, field
import os

load_dotenv()

API_KEY = os.getenv("BOT_API_KEY")

@dataclass
class Json:
    json: dict = field(default_factory=dict)
    result: list | None = field(default=None)
    last_message: dict | None = field(default=None)
    sender_information: dict | None = field(default=None)
    chat_id: int | None = field(default=None)
    is_bot: bool | None = field(default=None)
    first_name: str | None = field(default=None)
    second_name: str | None = field(default=None)
    text: str | None = field(default=None)

    def __post_init__(self):
        if self.json:
            self.result = self.json.get("result")
            if self.result:
                self.last_message = self.result[-1].get("message")
                if self.last_message:
                    self.sender_information = self.last_message.get("from")
                    self.chat_id = self.sender_information.get("id")
                    self.is_bot = self.sender_information.get("is_bot")
                    self.first_name = self.sender_information.get("first_name")
                    self.second_name = self.sender_information.get("last_name")
        if self.result and self.result[-1]:
            self.text = self.result[-1].get("text")

async def get_updates(session):
    async with session.get(f"https://api.telegram.org/bot{API_KEY}/getUpdates") as updates:
        updates_json = await updates.json()
        pprint(updates_json)
        return updates_json

async def send_message(session, chat_id, text):
    async with session.get(f"https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={chat_id}&text={text}") as response:  
        json = await response.json()
        pprint(json)

async def main():
    async with aiohttp.ClientSession() as session:
        result = Json(json=await get_updates(session))
        print(result.chat_id)
        print(result.first_name)
        print(result.is_bot)
        text = input()
        await send_message(session, result.chat_id, text)
        

if __name__ == "__main__":
    asyncio.run(main())            

