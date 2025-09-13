from abc import abstractmethod
from typing import Protocol


class TransactionManager(Protocol):
    """
    UoW-compatible interface for committing a business transaction.
    May be extended with rollback support.
    """

    @abstractmethod
    async def commit(self) -> None:
        """
        :raises DataMapperError:

        Commit the successful outcome of a business transaction.
        """
