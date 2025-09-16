from abc import abstractmethod
from typing import Protocol

from application.common.command_models.top_up_request import (
    TopUpRequestCreateCommandModel,
)
from domain.value_objects.top_up_request_id import TopUpRequestId


class TopUpRequestCommandGateway(Protocol):

    @abstractmethod
    async def add(
        self,
        top_up_request: TopUpRequestCreateCommandModel,
    ) -> TopUpRequestId: ...
