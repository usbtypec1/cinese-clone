from abc import abstractmethod
from typing import Protocol

from application.common.query_models.city import CityListQueryModel


class CityQueryGateway(Protocol):

    @abstractmethod
    async def read_all(self) -> list[CityListQueryModel]: ...
