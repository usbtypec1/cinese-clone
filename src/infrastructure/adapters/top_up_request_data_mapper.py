from dataclasses import dataclass
from typing import override

from sqlalchemy.ext.asyncio import AsyncSession

from application.common.command_models.top_up_request import (
    TopUpRequestCreateCommandModel,
)
from application.common.ports.top_up_request_command_gateway import (
    TopUpRequestCommandGateway,
)
from domain.enums.top_up_request_status import TopUpRequestStatus
from domain.value_objects.top_up_request_id import TopUpRequestId
from infrastructure.sqla.models.top_up_request import TopUpRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class SqlaTopUpRequestDataMapper(TopUpRequestCommandGateway):
    session: AsyncSession

    @override
    async def add(
        self,
        top_up_request: TopUpRequestCreateCommandModel,
    ) -> TopUpRequestId:
        request = TopUpRequest(
            amount=top_up_request.amount,
            user_id=top_up_request.user_id,
            receipt_file_id=top_up_request.receipt_file_id,
            status=TopUpRequestStatus.PENDING,
        )
        self.session.add(request)
        await self.session.flush()
        await self.session.refresh(request)
        return TopUpRequestId(request.id)
