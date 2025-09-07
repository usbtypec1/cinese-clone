from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateAdventisementInteractor:
    advertisement_repository: Any

    def execute(self) -> None:
        pass
