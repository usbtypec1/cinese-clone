from collections.abc import Iterable

from domain.entities.advertisement_photo import AdvertisementPhoto
from domain.entities.base import Entity
from domain.enums.advertisement_type import AdvertisementType
from domain.enums.delivery_option import DeliveryOption
from domain.enums.product_condition import ProductCondition
from domain.value_objects.advertisement_description import (
    AdvertisementDescription,
)
from domain.value_objects.advertisement_id import AdvertisementId
from domain.value_objects.advertisement_price import AdvertisementPrice
from domain.value_objects.city_id import CityId
from domain.value_objects.is_phone_number_visible import IsPhoneNumberVisible
from domain.value_objects.user_id import UserId


class Advertisement(Entity[AdvertisementId]):

    def __init__(
        self,
        *,
        id_: AdvertisementId,
        user_id: UserId,
        type_: AdvertisementType,
        description: AdvertisementDescription,
        product_condition: ProductCondition,
        price: AdvertisementPrice,
        delivery_option: DeliveryOption,
        city_id: CityId,
        is_phone_number_visible: IsPhoneNumberVisible,
        photos: Iterable[AdvertisementPhoto],
    ):
        super().__init__(id_=id_)
        self.user_id = user_id
        self.type = type_
        self.description = description
        self.product_condition = product_condition
        self.price = price
        self.delivery_option = delivery_option
        self.city_id = city_id
        self.is_phone_number_visible = is_phone_number_visible
        self.photos = tuple(photos)
