import logging
from dataclasses import dataclass

from application.common.ports.category_query_gateway import (
    CategoryQueryGateway,
)
from application.common.query_models.category import CategoryListQueryModel


logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True, kw_only=True)
class ListCategoriesResponse:
    categories: list[CategoryListQueryModel]


@dataclass(frozen=True, slots=True, kw_only=True)
class ListCategoriesQuery:
    category_query_gateway: CategoryQueryGateway

    async def execute(self) -> ListCategoriesResponse:
        logger.info(
            'List categories: started.',
        )
        categories: list[CategoryListQueryModel] = (
            await self.category_query_gateway.read_all()
        )
        response = ListCategoriesResponse(categories=categories)
        logger.info('List categories: done.')
        return response
