from dataclasses import dataclass
from decimal import Decimal


@dataclass
class TopUpRequestCreateCommandModel:
    amount: Decimal
    receipt_file_id: str
    user_id: int
