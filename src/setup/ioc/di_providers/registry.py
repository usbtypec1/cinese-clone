from dishka import Provider
from dishka.integrations.aiogram import AiogramProvider

from setup.ioc.di_providers.application import ApplicationProvider
from setup.ioc.di_providers.infrastructure import infrastructure_provider
from setup.ioc.di_providers.presentation import PresentationProvider
from setup.ioc.di_providers.settings import SettingsProvider


def get_providers() -> tuple[Provider, ...]:
    return (
        SettingsProvider(),
        ApplicationProvider(),
        infrastructure_provider(),
        PresentationProvider(),
        AiogramProvider(),
    )
