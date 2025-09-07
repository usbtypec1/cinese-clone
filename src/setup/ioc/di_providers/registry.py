from dishka import Provider

from setup.ioc.di_providers.settings import SettingsProvider
from setup.ioc.di_providers.application import ApplicationProvider


def get_providers() -> tuple[Provider, ...]:
    return (
        SettingsProvider(),
        ApplicationProvider(),
    )
