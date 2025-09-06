from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from presentation.telegram.ui.views.base import TextView


class PaymentsMenuView(TextView):
    text = "Выберите опцию:"
    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Пополнить баланс",
                    callback_data=f"top_up_balance",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Оплатить услугу",
                    callback_data=f"pay_for_service",
                ),
            ],
        ],
    )
