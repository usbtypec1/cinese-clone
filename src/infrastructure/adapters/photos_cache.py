from dataclasses import dataclass
from typing import override

from redis.asyncio import Redis

from application.common.ports.photos_cache_gateway import PhotosCacheGateway
from application.common.types import CurrentUserId


@dataclass(frozen=True, slots=True, kw_only=True)
class RedisPhotosCache(PhotosCacheGateway):
    redis: Redis
    user_id: CurrentUserId
    max_size: int = 10  # cache limit

    @property
    def key(self) -> str:
        return f'photos-cache-user:{self.user_id}'

    @override
    async def read_all(self) -> list[str]:
        # list is stored left → right in insertion order
        return await self.redis.lrange(self.key, 0, -1)

    @override
    async def remove_by_file_id(self, file_id: str) -> None:
        # remove all occurrences of file_id
        await self.redis.lrem(self.key, 0, file_id)

    @override
    async def add(self, file_id: str) -> None:
        # ensure uniqueness: remove if already exists
        await self.redis.lrem(self.key, 0, file_id)
        # push new file_id at the end (right)
        await self.redis.rpush(self.key, file_id)
        # keep only last max_size items
        await self.redis.ltrim(self.key, -self.max_size, -1)

    @override
    async def remove_all(self) -> None:
        await self.redis.delete(self.key)
