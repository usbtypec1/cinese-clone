from dataclasses import dataclass
from typing import override

from sqlalchemy.ext.asyncio import AsyncSession

from application.common.ports.user_query_gateway import UserQueryGateway
from domain.entities.user import User
from domain.value_objects.user_id import UserId
from domain.value_objects.user_name import UserName
from domain.value_objects.user_phone_number import UserPhoneNumber
from domain.value_objects.user_username import UserUsername
from infrastructure.sqla.models.user import User as SqlaUser


@dataclass(frozen=True, slots=True, kw_only=True)
class SqlaUserReader(UserQueryGateway):
    session: AsyncSession

    @override
    async def read_by_id(self, id_: int) -> User | None:
        user: SqlaUser | None = await self.session.get(SqlaUser, id_)
        if user is None:
            return None
        return User(
            id_=UserId(user.id),
            username=UserUsername(user.username),
            phone_number=UserPhoneNumber(user.phone_number),
            name=UserName(user.name),
        )
