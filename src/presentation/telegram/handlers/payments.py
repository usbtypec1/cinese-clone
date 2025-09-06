from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from presentation.telegram.filters.states import TopUpBalanceStates
from presentation.telegram.ui.views.base import answer_view
from presentation.telegram.ui.views.payments import PaymentsMenuView


payments_router = Router(name=__name__)


@payments_router.message(F.photo, StateFilter(TopUpBalanceStates.receipt))
async def on_top_up_balance_receipt_entered(
    message: F.Message,
    state: FSMContext,
) -> None:
    state_data = await state.get_data()
    amount = state_data["amount"]

    await state.clear()
    await answer_view(message, PaymentsMenuView())


@payments_router.message(StateFilter(TopUpBalanceStates.amount))
async def on_top_up_balance_amount_entered(
    message: F.Message,
    state: FSMContext,
) -> None:
    amount_text = message.text
    if not amount_text.isdigit() or int(amount_text) <= 0:
        await message.answer("Пожалуйста, введите корректную сумму (положительное число).")
        return

    amount = int(amount_text)
    await state.update_data(amount=amount)
    await state.set_state(TopUpBalanceStates.receipt)
    await message.answer(f"Вы ввели сумму: {amount}. Пожалуйста, отправьте квитанцию об оплате.")


@payments_router.callback_query(F.data == "top_up_balance")
async def on_top_up_balance_button(
    callback_query: CallbackQuery,
    state: FSMContext,
) -> None:
    await state.set_state(TopUpBalanceStates.amount)
    await callback_query.message.edit_text("Введите сумму для пополнения:")


@payments_router.callback_query(F.data == "payments")
async def on_payments_button(callback_query: CallbackQuery) -> None:
    await answer_view(callback_query.message, PaymentsMenuView())
