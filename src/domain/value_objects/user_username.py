from dataclasses import dataclass
from typing import ClassVar, Final

from domain.exceptions.base import DomainFieldError
from domain.value_objects.base import ValueObject


@dataclass(frozen=True, slots=True)
class UserUsername(ValueObject):
    """
    Raises:
        DomainFieldError.
    """
    MIN_LEN: ClassVar[Final[int]] = 1
    MAX_LEN: ClassVar[Final[int]] = 32

    value: str | None

    def __post_init__(self):
        super().__post_init__()
        self._validate_username_length()

    def _validate_username_length(self) -> None:
        if self.value is None:
            return
        length = len(self.value)
        if not (self.MIN_LEN <= length <= self.MAX_LEN):
            raise DomainFieldError(
                f'User username length must be between '
                f'{self.MIN_LEN} and {self.MAX_LEN} characters.',
            )
