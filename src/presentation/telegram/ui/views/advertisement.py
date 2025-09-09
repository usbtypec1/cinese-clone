from collections.abc import Iterable

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from infrastructure.sqla.models.advertisement import AdvertisementType
from presentation.telegram.filters.callback_data.advertisement.create import (
    AdvertisementTypeCallbackData,
)
from presentation.telegram.ui.views.base import TextView


class AdvertisementTypeListView(TextView):
    text = 'Выберите тип объявления:'
    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='🛒 Продаю',
                    callback_data=AdvertisementTypeCallbackData(
                        type=AdvertisementType.BUY,
                    ).pack(),
                ),
            ],
            [
                InlineKeyboardButton(
                    text='👀 Ищу',
                    callback_data=AdvertisementTypeCallbackData(
                        type=AdvertisementType.SELL,
                    ).pack(),
                ),
            ],
            [
                InlineKeyboardButton(
                    text='🔁 Обмен',
                    callback_data=AdvertisementTypeCallbackData(
                        type=AdvertisementType.EXCHANGE,
                    ).pack(),
                ),
            ],
        ],
    )


class AdvertisementCategoryListView(TextView):
    text = 'Выберите категорию:'

    def __init__(self, categories: Iterable):
        self.__categories = tuple(categories)


