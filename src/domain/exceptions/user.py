from domain.exceptions.base import DomainError
from domain.value_objects.user_id import UserId


class UserNotFoundByIdError(DomainError):
    def __init__(self, id_: UserId):
        super().__init__(f'User with id={id_.value} not found.')
