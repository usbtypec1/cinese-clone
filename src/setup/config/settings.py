import pathlib
import tomllib

from pydantic import BaseModel

from setup.config.database import DatabaseSettings
from setup.config.redis import RedisSettings
from setup.config.telegram_bot import TelegramBotSettings


class AppSettings(BaseModel):
    telegram_bot: TelegramBotSettings
    database: DatabaseSettings
    redis: RedisSettings


def load_app_settings() -> AppSettings:
    path = pathlib.Path(__file__).parents[3] / "settings.toml"
    settings = path.read_text(encoding="utf-8")
    return AppSettings.model_validate(tomllib.loads(settings))
