from decimal import Decimal

from sqlalchemy import ForeignKey, String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from domain.enums.advertisement_type import AdvertisementType
from domain.enums.delivery_option import DeliveryOption
from domain.enums.product_condition import ProductCondition
from infrastructure.sqla.models.base import Base


class Advertisement(Base):
    __tablename__ = 'advertisements'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'),
    )
    type: Mapped[AdvertisementType]
    title: Mapped[str] = mapped_column(String(64))
    description: Mapped[str] = mapped_column(String(512))
    product_condition: Mapped[ProductCondition]
    price: Mapped[Decimal]
    delivery_option: Mapped[DeliveryOption]
    city_id: Mapped[int] = mapped_column(
        ForeignKey('cities.id', ondelete='CASCADE'),
    )
    is_phone_number_visible: Mapped[bool]

    __table_args__ = (
        CheckConstraint(
            "price >= 0", name="ck_advertisements_price_non_negative",
        ),
    )
