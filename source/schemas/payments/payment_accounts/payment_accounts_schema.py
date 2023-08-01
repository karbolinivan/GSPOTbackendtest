from uuid import UUID

from pydantic import BaseModel

from source.enums.payments.currency import Currencies


class Payments_Accounts(BaseModel):
    user_uuid: UUID
    balance: float
    balance_currency: Currencies