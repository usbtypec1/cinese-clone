from abc import abstractmethod
from typing import Protocol


class TextsQueryGateway(Protocol):

    @abstractmethod
    async def read_rules_text(self) -> str | None: ...

    @abstractmethod
    async def read_support_text(self) -> str | None: ...

    @abstractmethod
    async def read_community_url(self) -> str | None: ...
