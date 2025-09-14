import asyncio
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dishka import make_async_container
from dishka.integrations.aiogram import setup_dishka

from presentation.telegram.handlers.registry import get_routers
from setup.config.settings import load_app_settings, AppSettings
from setup.ioc.di_providers.registry import get_providers


async def main() -> None:
    settings = load_app_settings()

    container = make_async_container(
        *get_providers(),
        context={AppSettings: settings},
    )

    bot = Bot(
        token=settings.telegram_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dispatcher = Dispatcher()
    dispatcher.include_routers(*get_routers())

    dispatcher['admin_user_ids'] = settings.telegram_bot.admin_chat_ids

    setup_dishka(container=container, router=dispatcher, auto_inject=True)

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
