from decimal import Decimal
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from domain.enums.transaction_type import TransactionType
from infrastructure.sqla.models.base import Base


class Transaction(Base):
    __tablename__ = 'transactions'

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'),
    )
    amount: Mapped[Decimal]
    description: Mapped[str] = mapped_column(String(255))
    type: Mapped[TransactionType]

    __table_args__ = (
        CheckConstraint("amount > 0", name="ck_transactions_amount_positive"),
    )
