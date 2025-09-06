from mailbox import Message

from aiogram.filters import invert_f
from aiogram.types import CallbackQuery


def admin_filter(
    message_or_callback_query: Message | CallbackQuery,
    admin_user_ids: set[int],
) -> bool:
    return message_or_callback_query.from_user.id in admin_user_ids


user_filter = invert_f(admin_filter)
