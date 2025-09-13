import logging
from dataclasses import dataclass

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from application.common.ports.flusher import Flusher
from infrastructure.exceptions.gateway import DataMapperError


logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True, kw_only=True)
class SqlaFlusher(Flusher):
    session: AsyncSession

    async def flush(self) -> None:
        """
        Raises:
            DataMapperError.
        """
        try:
            await self.session.flush()
            logger.debug('Database flush done.')
        except SQLAlchemyError as error:
            raise DataMapperError(f'Database flush error') from error
