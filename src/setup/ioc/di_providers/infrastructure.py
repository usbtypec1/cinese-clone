from dishka import Provider, Scope
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
)

from infrastructure.redis_provider import get_redis_client
from infrastructure.sqla.provider import (
    get_async_engine,
    get_async_session_factory,
    get_async_session,
)


class InfrastructureProvider(Provider):
    pass


def infrastructure_provider() -> InfrastructureProvider:
    provider = InfrastructureProvider()
    provider.provide(
        provides=AsyncEngine,
        scope=Scope.APP,
        source=get_async_engine,
    )
    provider.provide(
        provides=async_sessionmaker[AsyncSession],
        scope=Scope.APP,
        source=get_async_session_factory,
    )
    provider.provide(
        provides=AsyncSession,
        scope=Scope.REQUEST,
        source=get_async_session,
    )
    provider.provide(
        provides=Redis,
        scope=Scope.APP,
        source=get_redis_client,
    )
    return provider
