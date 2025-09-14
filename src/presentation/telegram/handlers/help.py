from aiogram import Router, F
from aiogram.types import CallbackQuery
from dishka import FromDishka

from application.queries.read_rules_text import ReadRulesTextQuery
from application.queries.read_support_text import ReadSupportTextQuery


help_router = Router(name=__name__)


@help_router.callback_query(F.data == 'support')
async def on_show_support_text(
    callback_query: CallbackQuery,
    read_support_text_query: FromDishka[ReadSupportTextQuery],
) -> None:
    text = await read_support_text_query.execute()
    if text is None:
        text = 'Текст не установлен'
    await callback_query.message.answer(text)
    await callback_query.answer()


@help_router.callback_query(F.data == 'rules')
async def on_show_rules_text(
    callback_query: CallbackQuery,
    read_rules_text_query: FromDishka[ReadRulesTextQuery],
) -> None:
    text = await read_rules_text_query.execute()
    if text is None:
        text = 'Текст не установлен'
    await callback_query.message.answer(text)
    await callback_query.answer()
