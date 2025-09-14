from dataclasses import dataclass
from decimal import Decimal

from application.common.command_models.advertisement import \
    AdvertisementCreateCommandModel
from application.common.ports.advertisement_command_gateway import \
    AdvertisementCommandGateway
from application.common.ports.flusher import Flusher
from application.common.ports.transaction_manager import TransactionManager


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateAdvertisementRequest:
    title: str
    description: str
    category_id: int
    price: Decimal


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateAdvertisementInteractor:
    advertisement_command_gateway: AdvertisementCommandGateway
    flusher: Flusher
    transaction_manager: TransactionManager

    async def execute(self, request_data: CreateAdvertisementRequest) -> None:
        advertisement = AdvertisementCreateCommandModel(
            title=request_data.title,
            description=request_data.description,
            category_id=request_data.category_id,
            price=request_data.price,
        )

        await self.advertisement_command_gateway.add(advertisement)
        await self.flusher.flush()
        await self.transaction_manager.commit()
