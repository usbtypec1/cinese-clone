from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateAdvertisementInteractor:
    advertisement_gateway: Any

    def execute(self) -> None:
        pass
