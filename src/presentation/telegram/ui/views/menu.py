from decimal import Decimal

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from domain.entities.user import User
from presentation.telegram.ui.views.base import TextView


class MenuView(TextView):

    def __init__(
        self,
        *,
        user: User,
        advertisements_count: int,
        balance: Decimal,
        start_text: str | None = None,
        community_url: str | None,
    ):
        self.user = user
        self.advertisements_count = advertisements_count
        self.balance = balance
        self.start_text = start_text or ''
        self.community_url = community_url

    def get_text(self) -> str:
        return (
            f"👋 Привет, {self.user.name.value}!\n\n"
            f"{self.start_text}\n\n"
            f"Размещено объявлений: {self.advertisements_count}\n"
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
        rows = [
            [create_advertisement_button],
            [view_advertisements_button, payments_button],
        ]
        support_button = InlineKeyboardButton(
            text="💬 Поддержка",
            callback_data="support",
        )
        row = [support_button]
        if self.community_url is not None:
            community_button = InlineKeyboardButton(
                text="🌐 Комьюнити",
                url=self.community_url,
            )
            row.append(community_button)
        rows.append(row)
        my_car_button = InlineKeyboardButton(
            text="🚗 Мой автомобиль",
            callback_data="my_car",
        )
        rules_button = InlineKeyboardButton(
            text="📜 Правила",
            callback_data="rules",
        )
        rows.append([my_car_button, rules_button])
        return InlineKeyboardMarkup(inline_keyboard=rows)


class AdminMenuView(TextView):
    text = 'Админ-панель'
    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Объявления',
                    callback_data='admin_advertisements',
                ),
                InlineKeyboardButton(
                    text='Пользователи',
                    callback_data='admin_users',
                ),
            ],
            [
                InlineKeyboardButton(
                    text='Тексты',
                    callback_data='admin_help_texts',
                )
            ]
        ],
    )


class AdminTextsMenuView(TextView):
    text = 'Тексты'
    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Поменять стартовый текст',
                    callback_data='admin_edit_start_text',
                ),
            ],
            [
                InlineKeyboardButton(
                    text='Поменять текст правил',
                    callback_data='admin_edit_rules_text',
                ),
            ],
            [
                InlineKeyboardButton(
                    text='Поменять текст поддержки',
                    callback_data='admin_edit_support_text',
                ),
            ],
            [
                InlineKeyboardButton(
                    text='Поменять ссылку на комьюнити',
                    callback_data='admin_edit_community_url',
                ),
            ],
        ],
    )
