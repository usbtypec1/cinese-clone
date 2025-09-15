from abc import abstractmethod
from typing import Protocol


class PhotosCacheGateway(Protocol):

    @abstractmethod
    async def add(self, file_id: str) -> None: ...

    @abstractmethod
    async def remove_by_file_id(self, file_id: str) -> None: ...

    @abstractmethod
    async def remove_all(self) -> None: ...

    @abstractmethod
    async def read_all(self) -> list[str]: ...
