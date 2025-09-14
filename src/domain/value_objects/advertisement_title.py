from dataclasses import dataclass
from typing import ClassVar, Final

from domain.exceptions.base import DomainFieldError
from domain.value_objects.base import ValueObject


@dataclass(frozen=True, slots=True)
class AdvertisementTitle(ValueObject):
    """
    Raises:
        DomainFieldError.
    """

    MIN_LEN: ClassVar[Final[int]] = 2
    MAX_LEN: ClassVar[Final[int]] = 64

    value: str

    def __post_init__(self):
        super(AdvertisementTitle, self).__post_init__()
        self._validate_title_length()

    def _validate_title_length(self) -> None:
        length = len(self.value)
        if not (self.MIN_LEN <= length <= self.MAX_LEN):
            raise DomainFieldError(
                f'Advertisement title length must be between '
                f'{self.MIN_LEN} and {self.MAX_LEN} characters.',
            )
