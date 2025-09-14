import logging
from collections.abc import AsyncIterator

from pydantic import RedisDsn
from redis.asyncio import Redis


logger = logging.getLogger(__name__)


async def get_redis_client(redis_dsn: RedisDsn) -> AsyncIterator[Redis]:
    redis = Redis.from_url(str(redis_dsn))
    logger.debug("Redis client created.")
    yield redis
    logger.debug("Closing Redis client...")
    await redis.close()
    logger.debug("Redis client closed.")
