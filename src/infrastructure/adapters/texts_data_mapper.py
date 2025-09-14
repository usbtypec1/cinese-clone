from dataclasses import dataclass
from typing import override

from redis.asyncio import Redis
from redis.exceptions import RedisError

from application.common.ports.texts_command_gateway import TextsCommandGateway
from infrastructure.exceptions.gateway import DataMapperError


@dataclass(frozen=True, slots=True, kw_only=True)
class RedisTextsDataMapper(TextsCommandGateway):
    redis: Redis

    @override
    async def set_rules_text(self, text: str) -> None:
        try:
            await self.redis.set('adbot:rules_text', text)
        except RedisError as error:
            raise DataMapperError('Failed to set rules text') from error

    @override
    async def set_support_text(self, text: str) -> None:
        try:
            await self.redis.set('adbot:support_text', text)
        except RedisError as error:
            raise DataMapperError('Failed to set support text') from error

    @override
    async def set_community_url(self, url: str) -> None:
        try:
            await self.redis.set('adbot:community_url', url)
        except RedisError as error:
            raise DataMapperError('Failed to set community URL') from error
