from decimal import Decimal

from sqlalchemy import ForeignKey, String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from domain.enums.advertisement_status import AdvertisementStatus
from domain.enums.advertisement_type import AdvertisementType
from domain.enums.delivery_option import DeliveryOption
from domain.enums.product_condition import ProductCondition
from infrastructure.sqla.models.advertisement_photo import AdvertisementPhoto
from infrastructure.sqla.models.base import Base
from infrastructure.sqla.models.category import Category
from infrastructure.sqla.models.city import City
from infrastructure.sqla.models.user import User


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
    status: Mapped[AdvertisementStatus]

    user: Mapped[User] = relationship('User', back_populates='advertisements')
    city: Mapped[City] = relationship('City', back_populates='advertisements')
    category: Mapped[Category] = relationship(
        'Category',
        back_populates='advertisements',
    )
    photos: Mapped[list[AdvertisementPhoto]] = relationship(
        'AdvertisementPhoto',
        back_populates='advertisement',
        cascade='all, delete-orphan',
    )

    __table_args__ = (
        CheckConstraint(
            "price >= 0", name="ck_advertisements_price_non_negative",
        ),
    )
