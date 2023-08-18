from uuid import UUID

from pydantic import BaseModel, Field


class PayoutData(BaseModel):
    account_number: str = Field(..., title='account_number', max_length=30)
    is_auto_payout: bool
    payout_type: str
    user_uuid: UUID
