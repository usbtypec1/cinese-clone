from domain.entities.base import Entity
from domain.value_objects.advertisement_id import AdvertisementId
from domain.value_objects.advertisement_photo_id import AdvertisementPhotoId
from domain.value_objects.file_id import FileId
from domain.value_objects.file_unique_id import FileUniqueId


class AdvertisementPhoto(Entity[AdvertisementId]):

    def __init__(
        self,
        *,
        id_: AdvertisementPhotoId,
        advertisement_id: AdvertisementId,
        file_id: FileId,
        file_unique_id: FileUniqueId,
    ):
        super().__init__(id_=id_)
        self.advertisement_id = advertisement_id
        self.file_id = file_id
        self.file_unique_id = file_unique_id
