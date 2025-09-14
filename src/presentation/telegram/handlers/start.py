from decimal import Decimal

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from dishka import FromDishka

from application.queries.read_advertisements_count import \
    ReadAdvertisementsCountQuery
from presentation.telegram.filters.permissions import user_filter, admin_filter
from presentation.telegram.ui.views.base import answer_view
from presentation.telegram.ui.views.menu import MenuView


user_start_router = Router(name=__name__)
user_start_router.message.filter(user_filter)

admin_start_router = Router(name=__name__)
admin_start_router.message.filter(admin_filter)


@user_start_router.message(CommandStart())
async def on_start_command(
    message: Message,
    read_advertisements_count_query: FromDishka[ReadAdvertisementsCountQuery],
) -> None:
    advertisements_count = await read_advertisements_count_query.execute(
        user_id=message.from_user.id,
    )
    view = MenuView(
        user=message.from_user,
        ads_count=advertisements_count,
        balance=Decimal(0),
    )
    await answer_view(message, view)
