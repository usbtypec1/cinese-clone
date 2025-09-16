from dataclasses import dataclass
from decimal import Decimal

from domain.value_objects.base import ValueObject


@dataclass(frozen=True, slots=True, kw_only=True)
class TopUpRequestAmount(ValueObject):
    value: Decimal
