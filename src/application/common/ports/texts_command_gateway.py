from abc import abstractmethod
from typing import Protocol


class TextsCommandGateway(Protocol):

    @abstractmethod
    async def set_rules_text(self, text: str) -> None: ...

    @abstractmethod
    async def set_support_text(self, text: str) -> None: ...

    @abstractmethod
    async def set_community_url(self, url: str) -> None: ...
