from dataclasses import dataclass

from application.common.ports.user_query_gateway import UserQueryGateway
from application.common.types import CurrentUserId
from domain.entities.user import User
from domain.exceptions.user import UserNotFoundByIdError
from domain.value_objects.user_id import UserId


@dataclass(frozen=True, slots=True, kw_only=True)
class ReadCurrentUserQuery:
    """
    Raises:
        UserNotFoundByIdError.
    """
    user_id: CurrentUserId
    user_query_gateway: UserQueryGateway

    async def execute(self) -> User:
        user: User | None = await self.user_query_gateway.read_by_id(
            id_=self.user_id,
        )
        if user is None:
            raise UserNotFoundByIdError(id_=UserId(self.user_id))
        return user
