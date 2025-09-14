from collections.abc import Sequence
from dataclasses import dataclass
from typing import override

from sqlalchemy import select, ScalarResult
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from application.common.ports.city_query_gateway import CityQueryGateway
from application.common.query_models.city import CityListQueryModel
from infrastructure.exceptions.gateway import ReaderError
from infrastructure.sqla.models.city import City


@dataclass(frozen=True, slots=True, kw_only=True)
class SqlaCityReader(CityQueryGateway):
    session: AsyncSession

    @override
    async def read_all(self) -> list[CityListQueryModel]:
        statement = select(City)

        try:
            result: ScalarResult[City] = await self.session.scalars(
                statement,
            )
            rows: Sequence[City] = result.all()

            return [
                CityListQueryModel(
                    id=row.id,
                    name=row.name,
                )
                for row in rows
            ]
        except SQLAlchemyError as error:
            raise ReaderError('Database query city failed.') from error
