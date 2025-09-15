from abc import abstractmethod
from typing import Protocol

from domain.entities.advertisement import Advertisement


class AdvertisementQueryGateway(Protocol):

    @abstractmethod
    async def read_by_id(self, id_: int) -> Advertisement: ...

    @abstractmethod
    async def count_of_user_advertisements(self, user_id: int) -> int: ...

    @abstractmethod
    async def read_all(
        self,
        *,
        user_id: int,
        limit: int,
        offset: int,
    ) -> list[Advertisement]: ...
