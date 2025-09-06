from decimal import Decimal

from aiogram.types import User, InlineKeyboardMarkup, InlineKeyboardButton

from presentation.telegram.ui.views.base import TextView


class MenuView(TextView):

    def __init__(self, user: User, ads_count: int, balance: Decimal):
        self.user = user
        self.ads_count = ads_count
        self.balance = balance

    def get_text(self) -> str:
        return (
            f"👋 Привет, {self.user.username or self.user.full_name}!\n\n"
            f"Шаблонный текст\n\n"
            f"Размещено объявлений: {self.ads_count}\n"
            f"Баланс: {self.balance} KGS"
        )

    def get_reply_markup(self) -> InlineKeyboardMarkup:
        create_advertisement_button = InlineKeyboardButton(
            text="🚀 Создать объявление",
            callback_data="create_advertisement",
        )
        view_advertisements_button = InlineKeyboardButton(
            text="📋 Мои объявления",
            callback_data="view_advertisements",
        )
        payments_button = InlineKeyboardButton(
            text="💵 Платежи",
            callback_data="payments",
        )
        support_button = InlineKeyboardButton(
            text="💬 Поддержка",
            callback_data="support",
        )
        community_button = InlineKeyboardButton(
            text="🌐 Комьюнити",
            url="https://t.me/your_community_link",
        )
        my_car_button = InlineKeyboardButton(
            text="🚗 Мой автомобиль",
            callback_data="my_car",
        )
        rules_button = InlineKeyboardButton(
            text="📜 Правила",
            callback_data="rules",
        )
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [create_advertisement_button],
                [view_advertisements_button, payments_button],
                [support_button, community_button],
                [my_car_button, rules_button],
            ],
        )
