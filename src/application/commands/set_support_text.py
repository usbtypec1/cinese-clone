from dataclasses import dataclass

from application.common.ports.texts_command_gateway import TextsCommandGateway


@dataclass(frozen=True, slots=True, kw_only=True)
class SetSupportTextCommand:
    texts_command_gateway: TextsCommandGateway

    async def execute(self, support_text: str) -> None:
        await self.texts_command_gateway.set_support_text(support_text)
