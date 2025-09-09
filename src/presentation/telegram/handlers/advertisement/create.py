from aiogram import Router, F
from aiogram.types import CallbackQuery


advertisement_create_router = Router(name=__name__)


@advertisement_create_router.callback_query(
    F.data == 'create_advertisement',
)
async def on_create_advertisement(callback_query: CallbackQuery) -> None:
    pass
