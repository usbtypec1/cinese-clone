from abc import abstractmethod
from typing import Protocol

from domain.entities.user import User


class UserCommandGateway(Protocol):

    @abstractmethod
    async def add(self, user: User) -> None: ...
