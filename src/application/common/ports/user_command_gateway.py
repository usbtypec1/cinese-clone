from abc import abstractmethod
from typing import Protocol


class UserCommandGateway(Protocol):

    @abstractmethod
    async def add(self, advertisement):