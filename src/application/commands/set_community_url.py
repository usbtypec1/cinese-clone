from dataclasses import dataclass

from application.common.ports.texts_command_gateway import TextsCommandGateway


@dataclass(frozen=True, slots=True, kw_only=True)
class SetCommunityUrlCommand:
    texts_command_gateway: TextsCommandGateway

    async def execute(self, community_url: str) -> None:
        await self.texts_command_gateway.set_community_url(community_url)
