import logging
from dataclasses import dataclass

from aiogram import Bot
from aiogram.exceptions import TelegramAPIError

from presentation.telegram.ui.views.base import View, send_view


logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True, kw_only=True)
class SendToTelegramAdminsInteractor:
    admin_chat_ids: set[int]
    bot: Bot

    async def execute(self, view: View) -> None:
        for chat_id in self.admin_chat_ids:
            try:
                await send_view(
                    bot=self.bot,
                    chat_id=chat_id,
                    view=view,
                )
            except TelegramAPIError as error:
                logger.error(
                    "Failed to send message to admin chat_id %s. Error %s",
                    chat_id,
                    error,
                )
