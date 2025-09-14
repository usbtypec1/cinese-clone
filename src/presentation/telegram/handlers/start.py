from decimal import Decimal

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from dishka import FromDishka

from application.queries.read_advertisements_count import \
    ReadAdvertisementsCountQuery
from application.queries.read_community_url import ReadCommunityUrlQuery
from application.queries.read_current_user import ReadCurrentUserQuery
from application.queries.read_start_text import ReadStartTextQuery
from domain.exceptions.user import UserNotFoundByIdError
from presentation.telegram.filters.permissions import user_filter, admin_filter
from presentation.telegram.filters.states import RegisterUserStates
from presentation.telegram.ui.views.base import answer_view
from presentation.telegram.ui.views.menu import MenuView
from presentation.telegram.ui.views.register_user import RegisterUserNameView


user_start_router = Router(name=__name__)
user_start_router.message.filter(user_filter)

admin_start_router = Router(name=__name__)
admin_start_router.message.filter(admin_filter)


@user_start_router.message(CommandStart())
async def on_start_command(
    message: Message,
    state: FSMContext,
    read_advertisements_count_query: FromDishka[ReadAdvertisementsCountQuery],
    read_start_text_query: FromDishka[ReadStartTextQuery],
    read_community_url_query: FromDishka[ReadCommunityUrlQuery],
    read_current_user_query: FromDishka[ReadCurrentUserQuery],
) -> None:
    try:
        await read_current_user_query.execute()
    except UserNotFoundByIdError:
        await state.set_state(RegisterUserStates.name)
        view = RegisterUserNameView()
        await answer_view(message, view)
        return

    advertisements_count = await read_advertisements_count_query.execute(
        user_id=message.from_user.id,
    )
    start_text = await read_start_text_query.execute()
    community_url = await read_community_url_query.execute()
    view = MenuView(
        user=message.from_user,
        advertisements_count=advertisements_count,
        start_text=start_text,
        balance=Decimal(0),
        community_url=community_url,
    )
    await answer_view(message, view)
