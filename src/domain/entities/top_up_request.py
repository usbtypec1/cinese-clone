from domain.entities.base import Entity
from domain.entities.user import User
from domain.enums.top_up_request_status import TopUpRequestStatus
from domain.value_objects.top_up_request_amount import TopUpRequestAmount
from domain.value_objects.top_up_request_id import TopUpRequestId
from domain.value_objects.top_up_request_receipt_file_id import (
    TopUpRequestReceiptFileId,
)


class TopUpRequest(Entity[TopUpRequestId]):

    def __init__(
        self,
        *,
        id_: TopUpRequestId,
        user: User,
        amount: TopUpRequestAmount,
        receipt_file_id: TopUpRequestReceiptFileId,
        status: TopUpRequestStatus,
    ):
        super().__init__(id_=id_)
        self.user = user
        self.amount = amount
        self.receipt_file_id = receipt_file_id
        self.status = status
