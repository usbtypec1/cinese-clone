from dataclasses import dataclass
from decimal import Decimal

from application.common.command_models.top_up_request import (
    TopUpRequestCreateCommandModel,
)
from application.common.ports.flusher import Flusher
from application.common.ports.top_up_request_command_gateway import (
    TopUpRequestCommandGateway,
)
from application.common.ports.transaction_manager import TransactionManager
from application.common.types import CurrentUserId
from domain.value_objects.top_up_request_id import TopUpRequestId


@dataclass(frozen=True, slots=True, kw_only=True)
class TopUpRequestRequest:
    amount: Decimal
    receipt_file_id: str


@dataclass(frozen=True, slots=True, kw_only=True)
class TopUpRequestResponse:
    top_up_request_id: int


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateTopUpRequestInteractor:
    top_up_request_command_gateway: TopUpRequestCommandGateway
    flusher: Flusher
    transaction_manager: TransactionManager
    user_id: CurrentUserId

    async def execute(
        self,
        request_data: TopUpRequestRequest,
    ) -> TopUpRequestResponse:
        request_id: TopUpRequestId = (
            await self.top_up_request_command_gateway.add(
                top_up_request=TopUpRequestCreateCommandModel(
                    amount=request_data.amount,
                    receipt_file_id=request_data.receipt_file_id,
                    user_id=self.user_id,
                ),
            )
        )
        await self.flusher.flush()
        await self.transaction_manager.commit()
        return TopUpRequestResponse(top_up_request_id=request_id.value)
