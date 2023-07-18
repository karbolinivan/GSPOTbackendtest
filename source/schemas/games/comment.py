from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field, StrictStr, StrictInt


class Comment(BaseModel):
    id: Optional[StrictInt] = Field(None, title='ID')
    userUuid: Optional[UUID] = Field(None, title='User uuid')
    createdAt: Optional[datetime] = Field(None, title='Created at')
    text: StrictStr = Field(..., title='Text', min_length=1)
