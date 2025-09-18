from aiogram.filters.callback_data import CallbackData


class TopUpRequestAcceptCallbackData(
    CallbackData,
    prefix='top_up_request_accept',
):
    top_up_request_id: int


class TopUpRequestRejectCallbackData(
    CallbackData,
    prefix='top_up_request_reject',
):
    top_up_request_id: int
