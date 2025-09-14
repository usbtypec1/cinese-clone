from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.sqla.models.base import Base


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    parent_id: Mapped[int | None] = mapped_column(
        ForeignKey('categories.id', ondelete='SET NULL'),
        default=None,
    )
    name: Mapped[str] = mapped_column(String(64))
    hashtag: Mapped[str] = mapped_column(String(32), unique=True)

    advertisements: Mapped[list["Advertisement"]] = relationship(
        back_populates="category",
        cascade="all, delete-orphan",
    )
