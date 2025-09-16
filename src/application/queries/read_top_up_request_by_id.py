from dataclasses import dataclass

from application.common.ports.top_up_request_query_gateway import (
    TopUpRequestQueryGateway,
)
from domain.entities.top_up_request import TopUpRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class ReadTopUpRequestByIdQuery:
    top_up_request_query_gateway: TopUpRequestQueryGateway

    async def execute(
        self,
        id_: int,
    ) -> TopUpRequest:
        top_up_request: TopUpRequest | None = (
            await self.top_up_request_query_gateway.read_by_id(id_=id_)
        )
        if top_up_request is None:
            raise
        return top_up_request
