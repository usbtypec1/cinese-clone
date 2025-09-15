from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from presentation.telegram.filters.permissions import admin_filter
from presentation.telegram.ui.views.base import answer_view
from presentation.telegram.ui.views.menu import AdminMenuView


admin_router = Router(name=__name__)


@admin_router.message(Command('admin'), admin_filter)
async def on_admin_command(message: Message):
    view = AdminMenuView()
    await answer_view(message, view)
