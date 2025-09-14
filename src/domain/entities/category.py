from domain.entities.base import Entity
from domain.value_objects.category_hashtag import CategoryHashtag
from domain.value_objects.category_id import CategoryId
from domain.value_objects.category_name import CategoryName


class Category(Entity[CategoryId]):

    def __init__(
        self,
        *,
        id_: CategoryId,
        name: CategoryName,
        hashtag: CategoryHashtag,
    ):
        super().__init__(id_=id_)
        self.name = name
        self.hashtag = hashtag
