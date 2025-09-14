from dishka import Provider, Scope, from_context, provide
from pydantic import PostgresDsn, RedisDsn

from setup.config.database import DatabaseSettings
from setup.config.settings import AppSettings
from setup.config.telegram_bot import TelegramBotSettings


class SettingsProvider(Provider):
    scope = Scope.APP

    settings = from_context(provides=AppSettings, scope=Scope.APP)

    @provide
    def provide_telegram_bot(
        self,
        settings: AppSettings,
    ) -> TelegramBotSettings:
        return settings.telegram_bot

    @provide
    def provide_database_settings(
        self,
        settings: AppSettings,
    ) -> DatabaseSettings:
        return settings.database

    @provide
    def provide_postgres_dsn(self, settings: AppSettings) -> PostgresDsn:
        return settings.database.dsn

    @provide
    def provide_redis_dsn(self, settings: AppSettings) -> RedisDsn:
        return settings.redis.dsn
