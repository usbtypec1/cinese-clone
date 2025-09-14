from aiogram.fsm.state import StatesGroup, State


class TopUpBalanceStates(StatesGroup):
    amount = State()
    receipt = State()


class AdvertisementCreateStates(StatesGroup):
    type = State()
    category = State()
    product_condition = State()
    title = State()
    description = State()
    photos = State()
    price = State()
    delivery_option = State()
    city = State()
    phone_number_visibility = State()
    confirm = State()
