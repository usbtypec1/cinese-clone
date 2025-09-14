from abc import abstractmethod
from typing import Protocol

from application.common.command_models.advertisement import (
    AdvertisementCreateCommandModel
)


class AdvertisementCommandGateway(Protocol):

    @abstractmethod
    async def add(
        self,
        advertisement: AdvertisementCreateCommandModel,
    ) -> None: ...
