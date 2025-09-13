import logging
from dataclasses import dataclass

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from application.common.ports.transaction_manager import TransactionManager
from infrastructure.exceptions.gateway import DataMapperError


logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True, kw_only=True)
class SqlaTransactionManager(TransactionManager):
    session: AsyncSession

    async def commit(self) -> None:
        """
        Raises:
            DataMapperError:
        """

        try:
            await self.session.commit()
            logger.debug('Database commit done.')
        except SQLAlchemyError as error:
            raise DataMapperError(f'Database commit error.') from error
