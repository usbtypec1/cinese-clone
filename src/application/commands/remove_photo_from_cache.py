from dataclasses import dataclass

from application.common.ports.photos_cache_gateway import PhotosCacheGateway
from application.common.types import CurrentUserId


@dataclass(frozen=True, slots=True, kw_only=True)
class RemovePhotoFromCacheInteractor:
    photos_cache_gateway: PhotosCacheGateway
    user_id: CurrentUserId

    async def execute(self, file_id: str) -> None:
        await self.photos_cache_gateway.remove_by_file_id(file_id)
