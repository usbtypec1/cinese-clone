from dataclasses import dataclass
from typing import override

from sqlalchemy import select, ScalarResult
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from application.common.ports.advertisement_query_gateway import (
    AdvertisementQueryGateway,
)
from domain.entities.advertisement import Advertisement
from domain.entities.advertisement_photo import AdvertisementPhoto
from domain.entities.category import Category
from domain.entities.city import City
from domain.entities.user import User
from domain.enums.advertisement_type import AdvertisementType
from domain.enums.delivery_option import DeliveryOption
from domain.enums.product_condition import ProductCondition
from domain.value_objects.advertisement_description import (
    AdvertisementDescription,
)
from domain.value_objects.advertisement_id import AdvertisementId
from domain.value_objects.advertisement_photo_id import AdvertisementPhotoId
from domain.value_objects.advertisement_price import AdvertisementPrice
from domain.value_objects.advertisement_title import AdvertisementTitle
from domain.value_objects.category_hashtag import CategoryHashtag
from domain.value_objects.category_id import CategoryId
from domain.value_objects.category_name import CategoryName
from domain.value_objects.city_id import CityId
from domain.value_objects.city_name import CityName
from domain.value_objects.file_id import FileId
from domain.value_objects.file_unique_id import FileUniqueId
from domain.value_objects.is_phone_number_visible import IsPhoneNumberVisible
from domain.value_objects.user_id import UserId
from domain.value_objects.user_name import UserName
from domain.value_objects.user_phone_number import UserPhoneNumber
from domain.value_objects.user_username import UserUsername
from infrastructure.exceptions.gateway import ReaderError
from infrastructure.sqla.models.advertisement import (
    Advertisement as SqlaAdvertisement,
)


@dataclass(frozen=True, slots=True, kw_only=True)
class SqlaAdvertisementReader(AdvertisementQueryGateway):
    session: AsyncSession

    @override
    async def read_by_id(self, id_: int) -> Advertisement | None:
        statement = (
            select(SqlaAdvertisement)
            .options(
                joinedload(
                    SqlaAdvertisement.user,
                    SqlaAdvertisement.city,
                    SqlaAdvertisement.category,
                    SqlaAdvertisement.photos,
                ),
            )
        )
        try:
            result: ScalarResult[SqlaAdvertisement] = (
                await self.session.scalars(statement)
            )
            row: SqlaAdvertisement | None = result.first()

            if row is None:
                return None

            return Advertisement(
                id_=AdvertisementId(row.id),
                user=User(
                    id_=UserId(row.user.id),
                    name=UserName(row.user.name),
                    username=UserUsername(row.user.username),
                    phone_number=UserPhoneNumber(row.user.phone_number),
                ),
                type_=AdvertisementType(row.type),
                title=AdvertisementTitle(row.title),
                description=AdvertisementDescription(row.description),
                product_condition=ProductCondition(row.product_condition),
                price=AdvertisementPrice(row.price),
                delivery_option=DeliveryOption(row.delivery_option),
                city=City(
                    id_=CityId(row.city.id),
                    name=CityName(row.city.name),
                ),
                category=Category(
                    id_=CategoryId(row.category.id),
                    name=CategoryName(row.category.name),
                    hashtag=CategoryHashtag(row.category.hashtag),
                ),
                is_phone_number_visible=IsPhoneNumberVisible(
                    row.is_phone_number_visible,
                ),
                photos=[
                    AdvertisementPhoto(
                        id_=AdvertisementPhotoId(photo.id),
                        advertisement_id=AdvertisementId(
                            photo.advertisement_id,
                        ),
                        file_id=FileId(photo.file_id),
                        file_unique_id=FileUniqueId(photo.file_unique_id),
                    )
                    for photo in row.photos
                ],
            )

        except SQLAlchemyError as error:
            raise ReaderError(
                'Database query advertisement by id failed.',
            ) from error
