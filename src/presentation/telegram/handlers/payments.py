from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from presentation.telegram.filters.states import TopUpBalanceStates
from presentation.telegram.ui.views.base import answer_view
from presentation.telegram.ui.views.payments import PaymentsMenuView


payments_router = Router(name=__name__)


@payments_router.callback_query(F.data == "payments")
async def on_payments_button(callback_query: CallbackQuery) -> None:
    await answer_view(callback_query.message, PaymentsMenuView())
