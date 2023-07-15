from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field, StrictStr, StrictInt, StrictBool


class Grade(Enum):
    LIKE = 'LIKE'
    DISLIKE = 'DISLIKE'


class Review(BaseModel):
    id: Optional[StrictInt] = Field(None, title='ID')
    reactions: Optional[StrictStr] = Field(None, title='Reactions')
    language: Optional[StrictStr] = Field(None, title='Language')
    userUuid: Optional[UUID] = Field(None, title='User uuid')
    text: StrictStr = Field(..., title='Text', min_length=1)
    grade: Grade = Field(..., title='Grade')
    viewType: Optional[StrictBool] = Field(None, title='View type')
    canReply: Optional[StrictBool] = Field(None, title='Can reply')
    createdAt: Optional[datetime] = Field(None, title='Created at')
