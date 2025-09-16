from dataclasses import dataclass

from domain.value_objects.base import ValueObject


@dataclass(frozen=True, slots=True)
class TopUpRequestReceiptFileId(ValueObject):
    value: str
