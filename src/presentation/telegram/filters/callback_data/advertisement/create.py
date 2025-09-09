from aiogram.filters.callback_data import CallbackData

from infrastructure.sqla.models.advertisement import AdvertisementType


class AdvertisementTypeCallbackData(CallbackData, prefix='advertisement-type'):
    type: AdvertisementType
