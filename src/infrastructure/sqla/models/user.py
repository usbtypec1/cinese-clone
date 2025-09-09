from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.sqla.models.base import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=False,
    )
    name: Mapped[str] = mapped_column(String(64))
    phone_number: Mapped[str] = mapped_column(String(20))
    username: Mapped[str | None] = mapped_column(String(32))
