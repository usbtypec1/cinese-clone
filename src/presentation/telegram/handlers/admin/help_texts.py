from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from dishka import FromDishka

from application.commands.set_community_url import SetCommunityUrlCommand
from application.commands.set_rules_text import SetRulesTextCommand
from application.commands.set_start_text import SetStartTextInteractor
from application.commands.set_support_text import SetSupportTextCommand
from presentation.telegram.filters.states import EditStartTextStates, \
    EditRulesTextStates, EditSupportTextStates, EditCommunityUrlStates
from presentation.telegram.ui.views.base import answer_view
from presentation.telegram.ui.views.menu import AdminTextsMenuView


admin_help_texts_router = Router(name=__name__)


@admin_help_texts_router.callback_query(
    F.data == 'admin_help_texts',
)
async def on_show_admin_help_texts_menu(callback_query: CallbackQuery) -> None:
    view = AdminTextsMenuView()
    await answer_view(callback_query.message, view)


@admin_help_texts_router.message(
    F.text,
    StateFilter(EditRulesTextStates.text),
)
async def on_rules_text_entered(
    message: Message,
    state: FSMContext,
    set_rules_text_interactor: FromDishka[SetRulesTextCommand]
) -> None:
    await set_rules_text_interactor.execute(rules_text=message.html_text)
    await state.clear()
    await message.answer('Текст правил успешно обновлен!')


@admin_help_texts_router.callback_query(
    F.data == 'admin_edit_rules_text',
)
async def on_edit_rules_text(
    callback_query: CallbackQuery,
    state: FSMContext,
) -> None:
    await state.set_state(EditRulesTextStates.text)
    await callback_query.message.answer('Введите новый текст правил:')
    await callback_query.answer()


@admin_help_texts_router.message(
    F.text,
    StateFilter(EditSupportTextStates.text),
)
async def on_support_text_entered(
    message: Message,
    state: FSMContext,
    set_support_text_interactor: FromDishka[SetSupportTextCommand]
) -> None:
    await set_support_text_interactor.execute(support_text=message.html_text)
    await state.clear()
    await message.answer('Текст поддержки успешно обновлен!')


@admin_help_texts_router.callback_query(
    F.data == 'admin_edit_support_text',
)
async def on_edit_support_text(
    callback_query: CallbackQuery,
    state: FSMContext,
) -> None:
    await state.set_state(EditSupportTextStates.text)
    await callback_query.message.answer('Введите новый текст поддержки:')
    await callback_query.answer()


@admin_help_texts_router.message(
    F.text,
    StateFilter(EditCommunityUrlStates.url),
)
async def on_community_url_entered(
    message: Message,
    state: FSMContext,
    set_community_url_interactor: FromDishka[SetCommunityUrlCommand]
) -> None:
    await set_community_url_interactor.execute(community_url=message.text)
    await state.clear()
    await message.answer('Ссылка на комьюнити успешно обновлена!')


@admin_help_texts_router.callback_query(
    F.data == 'admin_edit_community_url',
)
async def on_edit_community_url(
    callback_query: CallbackQuery,
    state: FSMContext,
) -> None:
    await state.set_state(EditCommunityUrlStates.url)
    await callback_query.message.answer('Введите новую ссылку на комьюнити:')
    await callback_query.answer()


@admin_help_texts_router.message(
    F.text,
    StateFilter(EditStartTextStates.text),
)
async def on_start_text_entered(
    message: Message,
    state: FSMContext,
    set_start_text_interactor: FromDishka[SetStartTextInteractor]
) -> None:
    await set_start_text_interactor.execute(start_text=message.html_text)
    await state.clear()
    await message.answer('Текст приветствия успешно обновлен!')


@admin_help_texts_router.callback_query(
    F.data == 'admin_edit_start_text',
)
async def on_edit_start_text(
    callback_query: CallbackQuery,
    state: FSMContext,
) -> None:
    await state.set_state(EditStartTextStates.text)
    await callback_query.message.answer('Введите новый текст приветствия:')
    await callback_query.answer()
