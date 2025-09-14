from dataclasses import dataclass
from typing import ClassVar, Final

from domain.exceptions.base import DomainFieldError
from domain.value_objects.base import ValueObject


@dataclass(frozen=True, slots=True)
class FileUniqueId(ValueObject):
    """
    Raises:
        DomainFieldError.
    """
    MIN_LEN: ClassVar[Final[int]] = 2
    MAX_LEN: ClassVar[Final[int]] = 256

    value: str

    def __post_init__(self):
        super(FileUniqueId, self).__post_init__()
        self._validate_unique_id_length()

    def _validate_unique_id_length(self) -> None:
        length = len(self.value)
        if not (self.MIN_LEN <= length <= self.MAX_LEN):
            raise DomainFieldError(
                f'File unique ID length must be between '
                f'{self.MIN_LEN} and {self.MAX_LEN} characters.',
            )
