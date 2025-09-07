from aiogram import Bot
from dishka import Provider, Scope, provide
from dishka.integrations.aiogram import AiogramMiddlewareData

from application.commands.send_to_admins import SendToTelegramAdminsInteractor
from setup.config.telegram_bot import TelegramBotSettings


class ApplicationProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def provide_send_to_admins_interactor(
        self,
        middleware_data: AiogramMiddlewareData,
        telegram_bot_settings: TelegramBotSettings,
    ) -> SendToTelegramAdminsInteractor:
        bot: Bot = middleware_data["bot"]
        return SendToTelegramAdminsInteractor(
            admin_chat_ids=telegram_bot_settings.admin_chat_ids,
            bot=bot,
        )
