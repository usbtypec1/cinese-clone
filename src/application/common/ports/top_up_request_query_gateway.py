from abc import abstractmethod
from typing import Protocol

from domain.entities.top_up_request import TopUpRequest


class TopUpRequestQueryGateway(Protocol):

    @abstractmethod
    async def read_by_id(self, id_: int) -> TopUpRequest: ...

    @abstractmethod
    async def read_all_pending(self) -> list[TopUpRequest]: ...
