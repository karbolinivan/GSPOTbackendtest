from typing import Optional

from pydantic import BaseModel, Field, StrictInt, StrictStr, validator, ValidationError

from source.enums.expected import ExpectedJSON


class Payments_Services(BaseModel):
    id: Optional[StrictInt] = Field(None, title='ID')
    name: StrictStr = Field(..., title='Name', min_length=1, max_length=30)

    @validator('name')
    def validate_name(cls, v):
        if not v.strip():
            raise ValidationError(ExpectedJSON.FIELD_CANNOT_BE_EMPTY.value)

        return v