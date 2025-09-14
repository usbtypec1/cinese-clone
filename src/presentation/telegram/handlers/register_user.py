import logging
from decimal import Decimal

from aiogram import Router, F
from aiogram.filters import ExceptionTypeFilter, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import ErrorEvent, Message, ReplyKeyboardRemove
from dishka import FromDishka

from application.commands.create_user import CreateUserInteractor, \
    CreateUserRequest
from application.queries.read_advertisements_count import \
    ReadAdvertisementsCountQuery
from application.queries.read_community_url import ReadCommunityUrlQuery
from application.queries.read_start_text import ReadStartTextQuery
from domain.exceptions.user import UserNotFoundByIdError
from presentation.telegram.filters.states import RegisterUserStates
from presentation.telegram.ui.views.base import answer_view
from presentation.telegram.ui.views.menu import MenuView
from presentation.telegram.ui.views.register_user import \
    RegisterUserPhoneNumberView


logger = logging.getLogger(__name__)

register_user_router = Router(name=__name__)


@register_user_router.error(
    ExceptionTypeFilter(UserNotFoundByIdError),
)
async def on_user_not_found_by_id_error(event: ErrorEvent) -> None:
    if event.update.message is not None:
        message = event.update.message
    elif event.update.callback_query is not None:
        message = event.update.callback_query.message
    else:
        logger.debug('User not found handler: invalid update type.')
        return


@register_user_router.message(
    F.text,
    StateFilter(RegisterUserStates.name),
)
async def on_user_name_entered(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(RegisterUserStates.phone_number)
    view = RegisterUserPhoneNumberView()
    await answer_view(message, view)


@register_user_router.message(
    F.contact,
    StateFilter(RegisterUserStates.phone_number),
)
async def on_user_phone_number_entered(
    message: Message,
    state: FSMContext,
    create_user_interactor: FromDishka[CreateUserInteractor],
    read_advertisements_count_query: FromDishka[ReadAdvertisementsCountQuery],
    read_start_text_query: FromDishka[ReadStartTextQuery],
    read_community_url_query: FromDishka[ReadCommunityUrlQuery],
) -> None:
    state_data: dict = await state.get_data()
    name = state_data['name']
    await create_user_interactor.execute(
        CreateUserRequest(
            id=message.from_user.id,
            name=name,
            username=message.from_user.username,
            phone_number=message.contact.phone_number,
        ),
    )
    await state.clear()
    await message.answer(
        'Вы успешно прошли регистрацию!',
        reply_markup=ReplyKeyboardRemove(),
    )

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
