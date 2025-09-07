from dishka import Provider, Scope, from_context, provide

from setup.config.settings import AppSettings
from setup.config.telegram_bot import TelegramBotSettings


class SettingsProvider(Provider):
    scope = Scope.APP

    settings = from_context(provides=AppSettings, scope=Scope.APP)

    @provide
    def provide_telegram_bot(self, settings: AppSettings) -> TelegramBotSettings:
        return settings.telegram_bot
