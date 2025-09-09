from dishka import Provider

from setup.ioc.di_providers.application import ApplicationProvider
from setup.ioc.di_providers.infrastructure import InfrastructureProvider
from setup.ioc.di_providers.settings import SettingsProvider


def get_providers() -> tuple[Provider, ...]:
    return (
        SettingsProvider(),
        ApplicationProvider(),
        InfrastructureProvider(),
    )
