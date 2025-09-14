from dataclasses import dataclass
from decimal import Decimal

from domain.exceptions.base import DomainFieldError
from domain.value_objects.base import ValueObject


@dataclass(frozen=True, slots=True)
class AdvertisementPrice(ValueObject):
    """
    Raises:
        DomainFieldError.
    """

    value: Decimal

    def __post_init__(self):
        super(AdvertisementPrice, self).__post_init__()
        self._validate_price_non_negative()

    def _validate_price_non_negative(self) -> None:
        if self.value < 0:
            raise DomainFieldError(
                'Advertisement price must be non-negative.',
            )
