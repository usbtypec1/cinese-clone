from dataclasses import dataclass
from typing import override

from sqlalchemy.ext.asyncio import AsyncSession

from application.common.ports.user_command_gateway import UserCommandGateway
from domain.entities.user import User


@dataclass(frozen=True, slots=True, kw_only=True)
class SqlaUserDataMapper(UserCommandGateway):
    session: AsyncSession

    @override
    async def add(self, user: User) -> None:
        self.session.add(user)
