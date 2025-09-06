from pydantic import BaseModel


class TelegramBotSettings(BaseModel):
    token: str
