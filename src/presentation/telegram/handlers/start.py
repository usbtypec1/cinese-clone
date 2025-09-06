from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart


start_router = Router(name=__name__)


@start_router.message(CommandStart())
async def on_start_command(message: Message) -> None:
    pass
