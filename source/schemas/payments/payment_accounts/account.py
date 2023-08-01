from uuid import UUID

from pydantic import BaseModel


class Account(BaseModel):
    user_uuid: UUID