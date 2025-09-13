from aiogram.filters.callback_data import CallbackData

from infrastructure.sqla.models.advertisement import (
    AdvertisementType,
    ProductCondition,
    DeliveryOption,
)


class AdvertisementTypeCallbackData(CallbackData, prefix='advertisement-type'):
    type: AdvertisementType


class AdvertisementCategoryCallbackData(
    CallbackData,
    prefix='advertisement-category',
):
    category_id: int


class AdvertisementProductConditionCallbackData(
    CallbackData,
    prefix='advertisement-product-condition',
):
    condition: ProductCondition


class AdvertisementDeliveryOptionCallbackData(
    CallbackData,
    prefix='advertisement-delivery-option',
):
    option: DeliveryOption


class AdvertisementCityCallbackData(CallbackData, prefix='advertisement-city'):
    city_id: int


class AdvertisementPhoneNumberVisibilityCallbackData(
    CallbackData,
    prefix='advertisement-phone-number-visibility',
):
    is_visible: bool