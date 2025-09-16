from aiogram import Router

from presentation.telegram.handlers.admin import admin_router
from presentation.telegram.handlers.advertisement import advertisement_router
from presentation.telegram.handlers.help import help_router
from presentation.telegram.handlers.payments import payments_router
from presentation.telegram.handlers.register_user import register_user_router
from presentation.telegram.handlers.start import user_start_router
from presentation.telegram.handlers.top_up_request import top_up_request_router


def get_routers() -> tuple[Router, ...]:
    return (
        help_router,
        register_user_router,
        user_start_router,
        payments_router,
        advertisement_router,
        admin_router,
        top_up_request_router,
    )
