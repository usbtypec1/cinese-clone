from dataclasses import dataclass

from application.common.ports.texts_query_gateway import TextsQueryGateway


@dataclass(frozen=True, slots=True, kw_only=True)
class ReadCommunityUrlCommand:
    texts_query_gateway: TextsQueryGateway

    async def execute(self) -> str | None:
        return await self.texts_query_gateway.read_community_url()
