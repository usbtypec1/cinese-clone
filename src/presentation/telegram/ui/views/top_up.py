from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from domain.entities.top_up_request import TopUpRequest
from presentation.telegram.filters.callback_data.top_up_request import \
    (
    TopUpRequestAcceptCallbackData, TopUpRequestRejectCallbackData,
)
from presentation.telegram.ui.views.base import (
    TextView, PhotoView,
    ReplyMarkup,
)


class TopUpAmountView(TextView):
    text = '💸 Введите сумму для пополнения:'


class TopUpReceiptView(TextView):

    def __init__(self, top_up_details_text: str):
        self.__top_up_details_text = top_up_details_text

    def get_text(self) -> str:
        return self.__top_up_details_text


class TopUpRequestSentView(TextView):
    text = '✅ Запрос на пополнение отправлен. Ожидайте подтверждения.'


class TopUpRequestDetailPhotoView(PhotoView):

    def __init__(self, top_up_request: TopUpRequest):
        self.__top_up_request = top_up_request

    def get_caption(self) -> str:
        return (
            f'Запрос на пополнение баланса:\n\n'
            f'Пользователь: {self.__top_up_request.user.name.value}'
            f' ({self.__top_up_request.user.phone_number.value})\n'
            f'Сумма: {self.__top_up_request.amount.value}'
        )

    def get_photo(self) -> str:
        return self.__top_up_request.receipt_file_id.value

    def get_reply_markup(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='✅ Одобрить',
                        callback_data=TopUpRequestAcceptCallbackData(
                            top_up_request_id=self.__top_up_request.id_.value,
                        ).pack(),
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text='❌ Отклонить',
                        callback_data=TopUpRequestRejectCallbackData(
                            top_up_request_id=self.__top_up_request.id_.value,
                        ).pack(),
                    )
                ]
            ],
        )
