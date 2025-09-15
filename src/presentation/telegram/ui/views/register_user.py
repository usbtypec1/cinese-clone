from aiogram.types import (
    ForceReply,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from presentation.telegram.ui.views.base import TextView


class UserNotRegisteredView(TextView):
    text = (
        '🎉 Добро пожаловать! 🎉\n\n'
        '🚀 Мы рады, что вы доверяете нам.\n\n'
        '😊 Давайте познакомимся?'
    )
    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='🤝 Начать знакомство',
                    callback_data='register_user_start',
                )
            ]
        ],
    )


class RegisterUserNameView(TextView):
    text = '☀️ Введите ваше имя:'


class RegisterUserPhoneNumberView(TextView):
    text = (
        '📲 Введите ваш номер телефона\n\n'
        'Для того нажмите на кнопку <b>📍 Отправить контактные данные</b>'
    )
    reply_markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(
                    text='📍 Отправить контактные данные',
                    request_contact=True,
                ),
            ],
        ],
    )
