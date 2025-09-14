from dataclasses import dataclass
from typing import override

from redis.asyncio import Redis
from redis.exceptions import RedisError

from application.common.ports.texts_query_gateway import TextsQueryGateway
from infrastructure.exceptions.gateway import ReaderError


@dataclass(frozen=True, slots=True, kw_only=True)
class RedisTextsReader(TextsQueryGateway):
    redis: Redis

    @override
    async def read_rules_text(self) -> str | None:
        try:
            return await self.redis.get('adbot:rules_text')
        except RedisError as error:
            raise ReaderError('Failed to get rules text') from error

    @override
    async def read_support_text(self) -> str | None:
        try:
            return await self.redis.get('adbot:support_text')
        except RedisError as error:
            raise ReaderError('Failed to get support text') from error

    @override
    async def read_community_url(self) -> str | None:
        try:
            return await self.redis.get('adbot:community_url')
        except RedisError as error:
            raise ReaderError('Failed to get community URL') from error

    @override
    async def read_start_text(self) -> str | None:
        try:
            return await self.redis.get('adbot:start_text')
        except RedisError as error:
            raise ReaderError('Failed to get start text') from error
