from aiogram import Router

from presentation.telegram.handlers.payments import payments_router
from presentation.telegram.handlers.start import start_router


def get_routers() -> tuple[Router, ...]:
    return (
        start_router,
        payments_router,
    )
