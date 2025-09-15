from aiogram import Router

from .help_texts import admin_help_texts_router
from .start import admin_start_router
from ...filters.permissions import admin_filter


admin_router = Router(name=__name__)
admin_router.message.filter(admin_filter)
admin_router.callback_query.filter(admin_filter)
admin_router.include_routers(
    admin_start_router,
    admin_help_texts_router,
)
