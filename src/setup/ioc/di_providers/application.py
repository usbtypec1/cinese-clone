from aiogram import Bot
from dishka import Provider, Scope, provide, provide_all
from dishka.integrations.aiogram import AiogramMiddlewareData

from application.commands.create_user import CreateUserInteractor
from application.commands.send_to_admins import SendToTelegramAdminsInteractor
from application.common.ports.flusher import Flusher
from application.common.ports.transaction_manager import TransactionManager
from infrastructure.adapters.flusher import SqlaFlusher
from infrastructure.adapters.transaction_manager import SqlaTransactionManager
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

    transaction_manager = provide(
        source=SqlaTransactionManager,
        provides=TransactionManager,
    )
    flusher = provide(
        source=SqlaFlusher,
        provides=Flusher,
    )

    commands = provide_all(
        CreateUserInteractor,
    )
