import asyncio

from aiogram import Bot, Dispatcher
from dishka import make_async_container
from dishka.integrations.aiogram import setup_dishka

from setup.config.settings import load_app_settings, AppSettings


async def main() -> None:
    settings = load_app_settings()

    container = make_async_container(
        context={AppSettings: settings},
    )

    bot = Bot(token=settings.telegram_bot.token)
    dispatcher = Dispatcher()

    setup_dishka(container=container, router=dispatcher, auto_inject=True)

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
