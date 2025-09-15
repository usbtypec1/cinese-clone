from abc import abstractmethod
from typing import Protocol

from application.common.command_models.category import (
    CategoryCreateCommandModel,
)


class CategoryCommandGateway(Protocol):

    @abstractmethod
    async def add(self, category: CategoryCreateCommandModel): ...
