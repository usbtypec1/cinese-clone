import logging
from dataclasses import dataclass

from application.common.ports.advertisement_query_gateway import (
    AdvertisementQueryGateway,
)


logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True, kw_only=True)
class ReadAdvertisementsCountQuery:
    advertisement_query_gateway: AdvertisementQueryGateway

    async def execute(self, user_id: int) -> int:
        logger.debug("Read advertisements count: started.")
        count = (
            await self.advertisement_query_gateway
            .count_of_user_advertisements(
                user_id=user_id,
            )
        )
        logger.debug("Read advertisements count: done.")
        return count
