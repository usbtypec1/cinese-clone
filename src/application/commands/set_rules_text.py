from dataclasses import dataclass

from application.common.ports.texts_command_gateway import TextsCommandGateway


@dataclass(frozen=True, slots=True, kw_only=True)
class SetRulesTextCommand:
    texts_command_gateway: TextsCommandGateway

    async def execute(self, rules_text: str) -> None:
        await self.texts_command_gateway.set_rules_text(rules_text)
