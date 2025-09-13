from domain.entities.base import Entity
from domain.value_objects.city_id import CityId
from domain.value_objects.city_name import CityName


class City(Entity[CityId]):

    def __init__(
        self,
        *,
        id_: CityId,
        name: CityName,
    ):
        super().__init__(id_=id_)
        self.name = name
