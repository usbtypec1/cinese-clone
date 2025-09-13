from dataclasses import dataclass

from application.common.ports.flusher import Flusher
from application.common.ports.transaction_manager import TransactionManager
from application.common.ports.user_command_gateway import UserCommandGateway
from domain.entities.user import User
from domain.value_objects.user_id import UserId
from domain.value_objects.user_name import UserName
from domain.value_objects.user_phone_number import UserPhoneNumber
from domain.value_objects.user_username import UserUsername


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateUserRequest:
    id: int
    name: str
    phone_number: str
    username: str | None


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateUserCommand:
    user_command_gateway: UserCommandGateway
    flusher: Flusher
    transaction_manager: TransactionManager

    async def execute(self, request_data: CreateUserRequest) -> None:
        user_id = UserId(request_data.id)
        name = UserName(request_data.name)
        phone_number = UserPhoneNumber(request_data.phone_number)
        username = UserUsername(request_data.username)

        user = User(
            id_=user_id,
            name=name,
            phone_number=phone_number,
            username=username,
        )

        await self.user_command_gateway.add(user)
        await self.flusher.flush()
        await self.transaction_manager.commit()
