from decimal import Decimal
from enum import StrEnum
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.sqla.models.base import Base
from infrastructure.sqla.models.city import City
from infrastructure.sqla.models.user import User


if TYPE_CHECKING:
    from infrastructure.sqla.models.advertisement_photo import (  # noqa: F401
        AdvertisementPhoto
    )


class AdvertisementType(StrEnum):
    SELL = 'sell'
    BUY = 'buy'
    EXCHANGE = 'exchange'


class ProductCondition(StrEnum):
    NEW = 'new'
    USED = 'used'


class DeliveryOption(StrEnum):
    NO_DELIVERY = 'no_delivery'
    COUNTRY = 'across_country'
    CIS = 'cis'
    WORLD = 'world'


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

    user: Mapped[User] = relationship(
        'User',
        back_populates='transactions',
    )
    photos: Mapped[list['AdvertisementPhoto']] = relationship(
        'AdvertisementPhoto',
        back_populates='advertisement',
        cascade='all, delete-orphan',
    )
    city: Mapped[City] = relationship(
        'City',
        back_populates='advertisements',
    )

    __table_args__ = (
        CheckConstraint(
            "amount >= 0", name="ck_advertisements_price_non_negative",
        ),
    )
