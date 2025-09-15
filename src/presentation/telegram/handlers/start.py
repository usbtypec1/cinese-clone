from decimal import Decimal

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from dishka import FromDishka

from application.queries.read_advertisements_count import (
    ReadAdvertisementsCountQuery,
)
from application.queries.read_community_url import ReadCommunityUrlQuery
from application.queries.read_current_user import ReadCurrentUserQuery
from application.queries.read_start_text import ReadStartTextQuery
from presentation.telegram.ui.views.base import answer_view
from presentation.telegram.ui.views.menu import MenuView


user_start_router = Router(name=__name__)


@user_start_router.message(CommandStart())
async def on_start_command(
    message: Message,
    read_advertisements_count_query: FromDishka[ReadAdvertisementsCountQuery],
    read_start_text_query: FromDishka[ReadStartTextQuery],
    read_community_url_query: FromDishka[ReadCommunityUrlQuery],
    read_current_user_query: FromDishka[ReadCurrentUserQuery],
) -> None:
    user = await read_current_user_query.execute()
    advertisements_count = await read_advertisements_count_query.execute(
        user_id=message.from_user.id,
    )
    start_text = await read_start_text_query.execute()
    community_url = await read_community_url_query.execute()
    view = MenuView(
        user=user,
        advertisements_count=advertisements_count,
        start_text=start_text,
        balance=Decimal(0),
        community_url=community_url,
    )
    await answer_view(message, view)
