from aiogram.fsm.state import StatesGroup, State


class TopUpBalanceStates(StatesGroup):
    amount = State()
    receipt = State()
