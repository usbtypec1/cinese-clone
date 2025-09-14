from dataclasses import dataclass
from typing import override

from sqlalchemy.ext.asyncio import AsyncSession

from application.common.ports.advertisement_command_gateway import (
    AdvertisementCommandGateway,
)
from domain.entities.advertisement import Advertisement


@dataclass(frozen=True, slots=True, kw_only=True)
class SqlaAdvertisementDataMapper(AdvertisementCommandGateway):
    session: AsyncSession

    @override
    async def add(self, advertisement: Advertisement) -> None:
        self.session.add(advertisement)
