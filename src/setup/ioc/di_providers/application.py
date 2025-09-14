from aiogram import Bot
from dishka import Provider, Scope, provide, provide_all
from dishka.integrations.aiogram import AiogramMiddlewareData

from application.commands.create_advertisement import (
    CreateAdvertisementInteractor,
)
from application.commands.create_user import CreateUserInteractor
from application.commands.read_community_url import ReadCommunityUrlCommand
from application.commands.read_rules_text import ReadRulesTextCommand
from application.commands.read_support_text import ReadSupportTextCommand
from application.commands.send_to_admins import SendToTelegramAdminsInteractor
from application.commands.set_community_url import SetCommunityUrlCommand
from application.commands.set_rules_text import SetRulesTextCommand
from application.commands.set_support_text import SetSupportTextCommand
from application.common.ports.advertisement_command_gateway import (
    AdvertisementCommandGateway,
)
from application.common.ports.advertisement_query_gateway import (
    AdvertisementQueryGateway,
)
from application.common.ports.category_query_gateway import (
    CategoryQueryGateway,
)
from application.common.ports.city_query_gateway import CityQueryGateway
from application.common.ports.flusher import Flusher
from application.common.ports.texts_command_gateway import TextsCommandGateway
from application.common.ports.texts_query_gateway import TextsQueryGateway
from application.common.ports.transaction_manager import TransactionManager
from application.common.ports.user_command_gateway import UserCommandGateway
from application.queries.list_categories import ListCategoriesQuery
from application.queries.list_cities import ListCitiesQuery
from application.queries.read_advertisement_by_id import (
    ReadAdvertisementByIdQuery,
)
from infrastructure.adapters.advertisement_data_mapper import (
    SqlaAdvertisementDataMapper,
)
from infrastructure.adapters.advertisement_reader import (
    SqlaAdvertisementReader,
)
from infrastructure.adapters.category_reader import SqlaCategoryReader
from infrastructure.adapters.city_reader import SqlaCityReader
from infrastructure.adapters.flusher import SqlaFlusher
from infrastructure.adapters.texts_data_mapper import RedisTextsDataMapper
from infrastructure.adapters.texts_reader import RedisTextsReader
from infrastructure.adapters.transaction_manager import SqlaTransactionManager
from infrastructure.adapters.user_data_mapper import SqlaUserDataMapper
from setup.config.telegram_bot import TelegramBotSettings


class ApplicationProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def provide_send_to_admins_interactor(
        self,
        middleware_data: AiogramMiddlewareData,
        telegram_bot_settings: TelegramBotSettings,
    ) -> SendToTelegramAdminsInteractor:
        bot: Bot = middleware_data["bot"]
        return SendToTelegramAdminsInteractor(
            admin_chat_ids=telegram_bot_settings.admin_chat_ids,
            bot=bot,
        )

    transaction_manager = provide(
        source=SqlaTransactionManager,
        provides=TransactionManager,
    )
    flusher = provide(
        source=SqlaFlusher,
        provides=Flusher,
    )

    # Command gateways
    user_command_gateway = provide(
        source=SqlaUserDataMapper,
        provides=UserCommandGateway,
    )
    advertisement_command_gateway = provide(
        source=SqlaAdvertisementDataMapper,
        provides=AdvertisementCommandGateway,
    )
    texts_command_gateway = provide(
        source=RedisTextsDataMapper,
        provides=TextsCommandGateway,
    )

    # Query gateways
    advertisement_query_gateway = provide(
        source=SqlaAdvertisementReader,
        provides=AdvertisementQueryGateway,
    )
    category_query_gateway = provide(
        source=SqlaCategoryReader,
        provides=CategoryQueryGateway,
    )
    city_query_gateway = provide(
        source=SqlaCityReader,
        provides=CityQueryGateway,
    )
    texts_query_gateway = provide(
        source=RedisTextsReader,
        provides=TextsQueryGateway,
    )

    commands = provide_all(
        CreateUserInteractor,
        CreateAdvertisementInteractor,
        SetRulesTextCommand,
        SetSupportTextCommand,
        SetCommunityUrlCommand,
    )

    queries = provide_all(
        ListCategoriesQuery,
        ListCitiesQuery,
        ReadAdvertisementByIdQuery,
        ReadRulesTextCommand,
        ReadSupportTextCommand,
        ReadCommunityUrlCommand,
    )
