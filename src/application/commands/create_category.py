from dataclasses import dataclass

from application.common.command_models.category import (
    CategoryCreateCommandModel,
)
from application.common.ports.category_command_gateway import (
    CategoryCommandGateway,
)


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateCategoryRequest:
    name: str
    hashtag: str


@dataclass(frozen=True, slots=True, kw_only=True)
class CreateCategoryInteractor:
    category_command_gateway: CategoryCommandGateway

    async def execute(self, request_data: CreateCategoryRequest) -> None:
        await self.category_command_gateway.add(
            CategoryCreateCommandModel(
                name=request_data.name,
                hashtag=request_data.hashtag,
            ),
        )
