import logging
from collections.abc import AsyncIterator

from pydantic import PostgresDsn
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)


log = logging.getLogger(__name__)


async def get_async_engine(
    dsn: PostgresDsn,
) -> AsyncIterator[AsyncEngine]:
    async_engine = create_async_engine(
        url=str(dsn),
        connect_args={"connect_timeout": 5},
        pool_pre_ping=True,
    )
    log.debug("Async engine created.")
    yield async_engine
    log.debug("Disposing async engine...")
    await async_engine.dispose()
    log.debug("Engine is disposed.")


def get_async_session_factory(
    engine: AsyncEngine,
) -> async_sessionmaker[AsyncSession]:
    async_session_factory = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        autoflush=False,
        expire_on_commit=False,
    )
    log.debug("Async session maker initialized.")
    return async_session_factory


async def get_async_session(
    async_session_factory: async_sessionmaker[AsyncSession],
) -> AsyncIterator[AsyncSession]:
    """Provides UoW (AsyncSession) for context."""
    log.debug("Starting Main async session...")
    async with async_session_factory() as session:
        log.debug("Main async session started.")
        yield session
        log.debug("Closing Main async session.")
    log.debug("Main async session closed.")
