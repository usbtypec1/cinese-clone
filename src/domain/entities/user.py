from domain.entities.base import Entity
from domain.value_objects.user_id import UserId
from domain.value_objects.user_name import UserName
from domain.value_objects.user_phone_number import UserPhoneNumber
from domain.value_objects.user_username import UserUsername


class User(Entity[UserId]):

    def __init__(
        self,
        *,
        id_: UserId,
        name: UserName,
        phone_number: UserPhoneNumber,
        username: UserUsername,
    ):
        super().__init__(id_=id_)
        self.name = name
        self.phone_number = phone_number
        self.username = username
