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


class RegisterUserStates(StatesGroup):
    name = State()
    phone_number = State()


class EditStartTextStates(StatesGroup):
    text = State()


class EditSupportTextStates(StatesGroup):
    text = State()


class EditCommunityUrlStates(StatesGroup):
    url = State()


class EditRulesTextStates(StatesGroup):
    text = State()


class TopUpRequestCreateStates(StatesGroup):
    amount = State()
    receipt = State()
