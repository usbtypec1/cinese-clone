from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from presentation.telegram.filters.states import TopUpRequestCreateStates
from presentation.telegram.ui.views.base import answer_view
from presentation.telegram.ui.views.top_up import TopUpAmountView, \
    TopUpRequestSentView, TopUpReceiptView


top_up_request_router = Router(name=__name__)


@top_up_request_router.message(
    F.photo | F.document,
    StateFilter(TopUpRequestCreateStates.receipt),
)
async def on_top_up_receipt_entered(
    message,
    state: FSMContext,
):
    if message.photo:
        receipt_file_id = message.photo[-1].file_id
    elif message.document:
        receipt_file_id = message.document.file_id
    else:
        return

    state_data: dict = await state.get_data()
    amount = state_data["amount"]

    await state.update_data(receipt_file_id=receipt_file_id)

    await state.clear()
    view = TopUpRequestSentView()
    await answer_view(message, view)


@top_up_request_router.message(
    F.text,
    StateFilter(TopUpRequestCreateStates.amount),
)
async def on_top_up_amount_entered(
    message,
    state: FSMContext,
):
    amount_text = message.text.replace(',', '.').strip()
    if not amount_text.isdigit() or float(amount_text) <= 0:
        await message.answer(
            "❗ Пожалуйста, введите корректную положительную сумму.",
        )
        return

    amount = str(amount_text)
    await state.update_data(amount=amount)
    await state.set_state(TopUpRequestCreateStates.receipt)
    view = TopUpReceiptView('test')
    await answer_view(message, view)


@top_up_request_router.callback_query(F.data == 'top_up_balance')
async def handle_top_up_request(
    callback_query: CallbackQuery,
    state: FSMContext,
):
    await state.set_state(TopUpRequestCreateStates.amount)
    view = TopUpAmountView()
    await answer_view(callback_query.message, view)
