from pydantic import BaseModel


class TelegramBotSettings(BaseModel):
    token: str
    admin_chat_ids: set[int]
