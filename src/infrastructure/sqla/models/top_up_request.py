from decimal import Decimal

from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from domain.enums.top_up_request_status import TopUpRequestStatus
from infrastructure.sqla.models.base import Base
from infrastructure.sqla.models.user import User


class TopUpRequest(Base):
    __tablename__ = 'top_up_requests'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'),
    )
    amount: Mapped[Decimal]
    status: Mapped[TopUpRequestStatus]
    receipt_file_id: Mapped[str]

    user: Mapped[User] = relationship('User', back_populates='top_up_requests')

    __table_args__ = (
        CheckConstraint(
            "amount > 0", name="ck_top_up_request_amount_positive",
        ),
    )
