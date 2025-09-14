from dataclasses import dataclass
from decimal import Decimal

from domain.enums.advertisement_type import AdvertisementType
from domain.enums.product_condition import ProductCondition


@dataclass
class AdvertisementCreateCommandModel:
    title: str
    description: str
    category_id: int
    price: Decimal
    type: AdvertisementType
    product_condition: ProductCondition
