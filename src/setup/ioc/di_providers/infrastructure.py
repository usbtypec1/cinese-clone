from collections.abc import AsyncIterator, AsyncGenerator

from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
)

from infrastructure.sqla.provider import (
    get_async_engine,
    get_async_session_factory,
)
from setup.config.database import DatabaseSettings


class InfrastructureProvider(Provider):

    @provide(scope=Scope.APP)
    def provide_async_engine(
        self,
        database_settings: DatabaseSettings,
    ) -> AsyncIterator[AsyncEngine]:
        return get_async_engine(database_settings.url)

    @provide(scope=Scope.APP)
    def provide_session_factory(
        self,
        engine: AsyncEngine,
    ) -> async_sessionmaker[AsyncSession]:
        return get_async_session_factory(engine)

    @provide(scope=Scope.REQUEST)
    async def provide_session(
        self,
        session_factory: async_sessionmaker[AsyncSession],
    ) -> AsyncGenerator[AsyncSession, None]:
        async with session_factory() as session:
            yield session
