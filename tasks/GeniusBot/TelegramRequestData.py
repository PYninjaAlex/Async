from dataclasses import dataclass, field


@dataclass
class TelegramRequestData:
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
