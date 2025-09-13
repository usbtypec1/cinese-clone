from dataclasses import dataclass

from domain.exceptions.base import DomainFieldError
from domain.value_objects.base import ValueObject


@dataclass(frozen=True, slots=True)
class AdvertisementPrice(ValueObject):
    """
    Raises:
        DomainFieldError.
    """

    value: int

    def __post_init__(self):
        super().__post_init__()
        self._validate_price_non_negative()

    def _validate_price_non_negative(self) -> None:
        if self.value < 0:
            raise DomainFieldError(
                'Advertisement price must be non-negative.',
            )
