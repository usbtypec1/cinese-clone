import logging
from dataclasses import dataclass

from application.common.ports.city_query_gateway import CityQueryGateway
from application.common.query_models.city import CityListQueryModel


logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True, kw_only=True)
class ListCitiesResponse:
    cities: list[CityListQueryModel]


@dataclass(frozen=True, slots=True, kw_only=True)
class ListCitiesQuery:
    city_query_gateway: CityQueryGateway

    async def execute(self) -> ListCitiesResponse:
        logger.info(
            'List cities: started.',
        )
        cities: list[CityListQueryModel] = (
            await self.city_query_gateway.read_all()
        )
        response = ListCitiesResponse(cities=cities)
        logger.info('List cities: done.')
        return response
