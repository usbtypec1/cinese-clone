import logging
from dataclasses import dataclass

from application.common.ports.advertisement_query_gateway import \
    AdvertisementQueryGateway
from domain.entities.advertisement import Advertisement
from domain.exceptions.advertisement import AdvertisementNotFoundByIdError
from domain.value_objects.advertisement_id import AdvertisementId


logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True, kw_only=True)
class ReadAdvertisementByIdQuery:
    advertisement_query_gateway: AdvertisementQueryGateway

    async def execute(self, id_: int) -> Advertisement:
        logger.info(
            'Read advertisement by id %s: started.',
            id_,
        )
        response = await self.advertisement_query_gateway.read_by_id(id_)

        if response is None:
            raise AdvertisementNotFoundByIdError(AdvertisementId(id_))

        logger.info('Read advertisement by id %s: done.', id_)
        return response
