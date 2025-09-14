from dataclasses import dataclass
from typing import override

from sqlalchemy.ext.asyncio import AsyncSession

from application.common.ports.user_command_gateway import UserCommandGateway
from domain.entities.user import User
from infrastructure.sqla.models.user import User as SqlaUser


@dataclass(frozen=True, slots=True, kw_only=True)
class SqlaUserDataMapper(UserCommandGateway):
    session: AsyncSession

    @override
    async def add(self, user: User) -> None:
        sqla_user = SqlaUser(
            id=user.id_.value,
            name=user.name.value,
            phone_number=user.phone_number.value,
            username=user.username.value,
        )
        self.session.add(sqla_user)
