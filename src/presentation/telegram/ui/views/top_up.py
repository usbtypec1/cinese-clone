from presentation.telegram.ui.views.base import TextView


class TopUpAmountView(TextView):
    text = '💸 Введите сумму для пополнения:'


class TopUpReceiptView(TextView):

    def __init__(self, top_up_details_text: str):
        self.top_up_details_text = top_up_details_text

    def get_text(self) -> str:
        return self.top_up_details_text


class TopUpRequestSentView(TextView):
    text = '✅ Запрос на пополнение отправлен. Ожидайте подтверждения.'
