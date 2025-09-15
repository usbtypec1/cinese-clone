from dataclasses import dataclass

from application.common.ports.advertisement_query_gateway import (
    AdvertisementQueryGateway,
)
from domain.entities.advertisement import Advertisement


@dataclass(frozen=True, slots=True, kw_only=True)
class ListAdvertisementsResponse:
    advertisements: list[Advertisement]
    limit: int
    offset: int


@dataclass(frozen=True, slots=True, kw_only=True)
class ListAdvertisementsQuery:
    advertisement_query_gateway: AdvertisementQueryGateway

    async def execute(
        self,
        *,
        user_id: int,
        limit: int,
        offset: int,
    ) -> ListAdvertisementsResponse:
        advertisements = await self.advertisement_query_gateway.read_all(
            limit=limit,
            offset=offset,
        )
        return ListAdvertisementsResponse(
            advertisements=advertisements,
            limit=limit,
            offset=offset,
        )
