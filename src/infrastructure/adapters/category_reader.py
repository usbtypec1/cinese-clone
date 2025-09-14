from collections.abc import Sequence
from dataclasses import dataclass
from typing import override

from sqlalchemy import select, ScalarResult
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from application.common.ports.category_query_gateway import (
    CategoryQueryGateway,
)
from application.common.query_models.category import CategoryListQueryModel
from infrastructure.exceptions.gateway import ReaderError
from infrastructure.sqla.models.category import Category


@dataclass(frozen=True, slots=True, kw_only=True)
class SqlaCategoryReader(CategoryQueryGateway):
    session: AsyncSession

    @override
    async def read_all(self) -> list[CategoryListQueryModel]:
        statement = select(Category)

        try:
            result: ScalarResult[Category] = await self.session.scalars(
                statement,
            )
            rows: Sequence[Category] = result.all()

            return [
                CategoryListQueryModel(
                    id=row.id,
                    name=row.name,
                    hashtag=row.hashtag,
                )
                for row in rows
            ]
        except SQLAlchemyError as error:
            raise ReaderError('Database query categories failed.') from error
