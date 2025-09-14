from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
)

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
    return provider
