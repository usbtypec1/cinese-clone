from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from domain.enums.advertisement_type import AdvertisementType
from domain.enums.delivery_option import DeliveryOption
from domain.enums.product_condition import ProductCondition
from infrastructure.sqla.models.base import Base


if TYPE_CHECKING:
    from infrastructure.sqla.models.advertisement_photo import (  # noqa: F401
        AdvertisementPhoto
    )
    from infrastructure.sqla.models.city import City  # noqa: F401
    from infrastructure.sqla.models.user import User  # noqa: F401


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

    user: Mapped['User'] = relationship(
        'User',
        back_populates='transactions',
    )
    photos: Mapped[list['AdvertisementPhoto']] = relationship(
        'AdvertisementPhoto',
        back_populates='advertisement',
        cascade='all, delete-orphan',
    )
    city: Mapped['City'] = relationship(
        'City',
        back_populates='advertisements',
    )

    __table_args__ = (
        CheckConstraint(
            "price >= 0", name="ck_advertisements_price_non_negative",
        ),
    )
