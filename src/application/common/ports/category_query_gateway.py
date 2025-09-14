from abc import abstractmethod
from typing import Protocol

from application.common.query_models.category import CategoryListQueryModel


class CategoryQueryGateway(Protocol):

    @abstractmethod
    async def read_all(self) -> list[CategoryListQueryModel]: ...
