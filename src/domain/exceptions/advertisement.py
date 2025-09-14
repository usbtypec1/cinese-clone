from domain.exceptions.base import DomainError
from domain.value_objects.advertisement_id import AdvertisementId


class AdvertisementNotFoundByIdError(DomainError):
    def __init__(self, id_: AdvertisementId):
        super().__init__(f'Advertisement with id={id_.value} not found.')
