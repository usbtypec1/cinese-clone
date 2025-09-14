from aiogram.types import ForceReply, ReplyKeyboardMarkup, KeyboardButton

from presentation.telegram.ui.views.base import TextView


class RegisterUserNameView(TextView):
    text = 'Приветствую! Для начала, введите ваше имя:'
    reply_markup = ForceReply(input_field_placeholder='Ваше имя')


class RegisterUserPhoneNumberView(TextView):
    text = 'Введите ваш номер телефона:'
    reply_markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(
                    text='Отправить номер телефона',
                    request_contact=True,
                ),
            ],
        ],
    )
