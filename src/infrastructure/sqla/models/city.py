from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.sqla.models.base import Base


class City(Base):
    __tablename__ = 'cities'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    name: Mapped[str] = mapped_column(String(128), unique=True)
