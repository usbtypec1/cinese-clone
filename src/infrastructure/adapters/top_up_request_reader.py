from dataclasses import dataclass
from typing import override

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from application.common.ports.top_up_request_query_gateway import (
    TopUpRequestQueryGateway,
)
from domain.entities.top_up_request import TopUpRequest
from domain.entities.user import User
from domain.enums.top_up_request_status import TopUpRequestStatus
from domain.value_objects.top_up_request_amount import TopUpRequestAmount
from domain.value_objects.top_up_request_id import TopUpRequestId
from domain.value_objects.top_up_request_receipt_file_id import \
    TopUpRequestReceiptFileId
from domain.value_objects.user_id import UserId
from domain.value_objects.user_name import UserName
from domain.value_objects.user_phone_number import UserPhoneNumber
from domain.value_objects.user_username import UserUsername
from infrastructure.sqla.models.top_up_request import \
    TopUpRequest as SqlaTopUpRequest


@dataclass(frozen=True, slots=True, kw_only=True)
class SqlaTopUpRequestReader(TopUpRequestQueryGateway):
    session: AsyncSession

    @override
    async def read_by_id(self, id_: int) -> TopUpRequest | None:
        statement = select(SqlaTopUpRequest).where(
            SqlaTopUpRequest.id == id_,
        ).options(
            joinedload(SqlaTopUpRequest.user),
        )
        result: SqlaTopUpRequest | None = await self.session.scalar(statement)
        if result is None:
            return None
        return TopUpRequest(
            id_=TopUpRequestId(result.id),
            user=User(
                id_=UserId(result.user.id),
                name=UserName(result.user.name),
                phone_number=UserPhoneNumber(result.user.phone_number),
                username=UserUsername(result.user.username),
            ),
            amount=TopUpRequestAmount(result.amount),
            receipt_file_id=TopUpRequestReceiptFileId(result.receipt_file_id),
            status=TopUpRequestStatus(result.status),
        )

    @override
    async def read_all_pending(self) -> list[TopUpRequest]:
        statement = select(SqlaTopUpRequest).where(
            SqlaTopUpRequest.status == TopUpRequestStatus.PENDING,
        ).options(
            joinedload(SqlaTopUpRequest.user),
        )
        result = await self.session.scalars(statement)
        return [
            TopUpRequest(
                id_=TopUpRequestId(row.id),
                user=User(
                    id_=UserId(row.user.id),
                    name=UserName(row.user.name),
                    phone_number=UserPhoneNumber(row.user.phone_number),
                    username=UserUsername(row.user.username),
                ),
                amount=TopUpRequestAmount(row.amount),
                receipt_file_id=TopUpRequestReceiptFileId(row.receipt_file_id),
                status=TopUpRequestStatus(row.status),
            )
            for row in result
        ]
