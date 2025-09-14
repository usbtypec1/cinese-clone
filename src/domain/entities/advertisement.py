from collections.abc import Iterable

from domain.entities.advertisement_photo import AdvertisementPhoto
from domain.entities.base import Entity
from domain.entities.category import Category
from domain.entities.city import City
from domain.entities.user import User
from domain.enums.advertisement_type import AdvertisementType
from domain.enums.delivery_option import DeliveryOption
from domain.enums.product_condition import ProductCondition
from domain.value_objects.advertisement_description import (
    AdvertisementDescription,
)
from domain.value_objects.advertisement_id import AdvertisementId
from domain.value_objects.advertisement_price import AdvertisementPrice
from domain.value_objects.advertisement_title import AdvertisementTitle
from domain.value_objects.is_phone_number_visible import IsPhoneNumberVisible


class Advertisement(Entity[AdvertisementId]):

    def __init__(
        self,
        *,
        id_: AdvertisementId,
        user: User,
        type_: AdvertisementType,
        title: AdvertisementTitle,
        description: AdvertisementDescription,
        product_condition: ProductCondition,
        price: AdvertisementPrice,
        delivery_option: DeliveryOption,
        city: City,
        is_phone_number_visible: IsPhoneNumberVisible,
        photos: Iterable[AdvertisementPhoto],
        category: Category,
    ):
        super().__init__(id_=id_)
        self.user = user
        self.type = type_
        self.title = title
        self.description = description
        self.product_condition = product_condition
        self.price = price
        self.delivery_option = delivery_option
        self.city = city
        self.is_phone_number_visible = is_phone_number_visible
        self.photos = tuple(photos)
        self.category = category
