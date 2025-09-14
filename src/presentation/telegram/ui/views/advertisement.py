from collections.abc import Iterable

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from domain.entities.advertisement import Advertisement
from infrastructure.sqla.models.advertisement import (
    AdvertisementType,
    ProductCondition,
    DeliveryOption,
)
from presentation.telegram.filters.callback_data.advertisement.create import (
    AdvertisementTypeCallbackData,
    AdvertisementCategoryCallbackData,
    AdvertisementProductConditionCallbackData,
    AdvertisementDeliveryOptionCallbackData,
    AdvertisementCityCallbackData,
    AdvertisementPhoneNumberVisibilityCallbackData,
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

    def get_reply_markup(self) -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardBuilder()
        for category in self.__categories:
            keyboard.button(
                text=category.name,
                callback_data=AdvertisementCategoryCallbackData(
                    category_id=category.id,
                ),
            )
        keyboard.adjust(1)
        return keyboard.as_markup()


class AdvertisementProductTitleView(TextView):
    text = (
        '🎇 Введите наименование товара\n\n'
        'Коротко опишите товар (название, бренд, модель, год и тп)\n\n'
        'Например: <b>Subaru Outback 2021.</b>'
    )


class AdvertisementProductConditionView(TextView):
    text = '🤩 Выберите состояние товара'
    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Новый',
                    callback_data=AdvertisementProductConditionCallbackData(
                        condition=ProductCondition.NEW,
                    ).pack(),
                ),
                InlineKeyboardButton(
                    text='Не новый',
                    callback_data=AdvertisementProductConditionCallbackData(
                        condition=ProductCondition.USED,
                    ).pack(),
                )
            ]
        ],
    )


class AdvertisementProductPhotosView(TextView):
    text = (
        '📸 Пришлите фотографии товара\n\n'
        'Можно отправить несколько фотографий'
        ' как альбом в одном сообщении при этом <b>не более 10 штук</b>'
    )


class AdvertisementProductDescriptionView(TextView):
    text = (
        '🖊️ Введите описание товара\n\n'
        'Более подробно опишите свой товар в произвольной форме\n\n'
        'Например: рама и вилка сталь, размер 52, все остальное стоковое,'
        ' состояние хорошее, есть царапины.'
    )


class AdvertisementProductPriceView(TextView):
    text = (
        '💵 Введите цену товара\n\n'
        'Напишите цену числом без указания валюты\n\n'
        'Например: 16000'
    )


class AdvertisementDeliveryOptionView(TextView):
    text = '🚚 Выберите вариант доставки:'
    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='🚫 Без доставки',
                    callback_data=AdvertisementDeliveryOptionCallbackData(
                        option=DeliveryOption.NO_DELIVERY,
                    ).pack(),
                ),
            ],
            [
                InlineKeyboardButton(
                    text='🌍 По стране',
                    callback_data=AdvertisementDeliveryOptionCallbackData(
                        option=DeliveryOption.COUNTRY,
                    ).pack(),
                ),
            ],
            [
                InlineKeyboardButton(
                    text='🌍 По СНГ',
                    callback_data=AdvertisementDeliveryOptionCallbackData(
                        option=DeliveryOption.CIS,
                    ).pack(),
                ),
            ],
            [
                InlineKeyboardButton(
                    text='🌏 По всему миру',
                    callback_data=AdvertisementDeliveryOptionCallbackData(
                        option=DeliveryOption.WORLD,
                    ).pack(),
                ),
            ],
        ],
    )


class AdvertisementCityListView(TextView):
    text = '🏙️ Выберите город:'

    def __init__(self, cities: Iterable):
        self.__cities = tuple(cities)

    def get_reply_markup(self) -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardBuilder()
        for city in self.__cities:
            keyboard.button(
                text=city.name,
                callback_data=AdvertisementCityCallbackData(city_id=city.id),
            )
        keyboard.adjust(1)
        return keyboard.as_markup()


class AdvertisementPhoneNumberView(TextView):
    text = '📱 Хотите показать свой номер телефона в объявлении?'
    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Да',
                    callback_data=AdvertisementPhoneNumberVisibilityCallbackData(
                        is_visible=True,
                    ).pack(),
                ),
            ],
            [
                InlineKeyboardButton(
                    text='Нет',
                    callback_data=AdvertisementPhoneNumberVisibilityCallbackData(
                        is_visible=False,
                    ).pack(),
                )
            ]
        ],
    )


class AdvertisementCreateConfirmView(TextView):
    text = '👍 Ваше объявление создано и готово к отправке!'
    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='✅ Опубликовать',
                    callback_data='publish_advertisement',
                ),
            ],
            [
                InlineKeyboardButton(
                    text='❌ Отменить',
                    callback_data='cancel_advertisement',
                ),
            ],
        ],
    )


class AdvertisementView(TextView):

    def __init__(
        self,
        advertisement: Advertisement,
    ):
        self.__advertisement = advertisement

    def get_text(self) -> str:
        lines = [
            f'#{self.__advertisement.category.hashtag.value}',
            f'{self.__advertisement.type},'
            f' {self.__advertisement.product_condition.value}'
            f' | {self.__advertisement.id_.value}',
            f'{self.__advertisement.user.name.value},'
            f' {self.__advertisement.city.name.value}',
            f'<b>{self.__advertisement.title.value}</b>',
            f'<i>{self.__advertisement.description.value}</i>\n',
            f'{self.__advertisement.price.value} KGS |'
            f' {self.__advertisement.delivery_option.value}\n',
        ]
        if self.__advertisement.is_phone_number_visible.value:
            lines.append(
                '📲 <span class="tg-spoiler">'
                f'{self.__advertisement.user.phone_number.value}</span>\n',
            )
        else:
            lines.append(f'📲 <span class="tg-spoiler">Скрыт</span>\n')
        lines.append('📢 Разместить объявление')
        if self.__advertisement.user.username.value is not None:
            lines.append(
                f' @'
                f'{self.__advertisement.user.username.value}',
            )
        return '\n'.join(lines)
