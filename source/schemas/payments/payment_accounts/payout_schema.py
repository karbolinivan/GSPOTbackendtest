from pydantic import BaseModel


class Amount(BaseModel):
    value: int
    currency: str


class PayoutDestinationData(BaseModel):
    type_: str
    account_number: str


class BaseRequestModel(BaseModel):
    amount: Amount
    payout_destination_data: PayoutDestinationData
    user_uuid: str
