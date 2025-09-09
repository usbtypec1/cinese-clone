from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.sqla.models.advertisement import Advertisement
from infrastructure.sqla.models.base import Base


class AdvertisementPhoto(Base):
    __tablename__ = 'advertisement_photos'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    advertisement_id: Mapped[int] = mapped_column(
        ForeignKey('advertisements.id', ondelete='CASCADE'),
    )
    file_id: Mapped[str]
    file_unique_id: Mapped[str]

    advertisement: Mapped[Advertisement] = relationship(
        'Advertisement',
        back_populates='photos',
    )
