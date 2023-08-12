from uuid import UUID

from pydantic import BaseModel


class Increase_Balance(BaseModel):
    payment_type: str
    payment_service: str
    payment_amount: int
    user_uuid: UUID
    return_url: str