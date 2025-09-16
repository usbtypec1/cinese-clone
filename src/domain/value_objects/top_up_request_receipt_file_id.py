from dataclasses import dataclass

from domain.value_objects.base import ValueObject


@dataclass(frozen=True, slots=True, kw_only=True)
class TopUpRequestReceiptFileId(ValueObject):
    value: str
