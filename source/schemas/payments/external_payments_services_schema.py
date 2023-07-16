from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator, ValidationError, root_validator

from source.api.payments.payments import get_services_list
from source.enums.expected import ExpectedJSON


class External_Payments(BaseModel):
    id: Optional[StrictInt] = Field(None, title='ID')
    name: StrictStr = Field(..., title='Name', min_length=1, max_length=30)

    @validator('name')
    def validate_name(cls, v):
        if not v.strip():
            raise ValidationError(ExpectedJSON.FIELD_CANNOT_BE_EMPTY.value)

        existing_services = get_services_list()
        if v in existing_services:
            raise ValidationError(ExpectedJSON.PAYMENT_SERVICE_WITH_THIS_NAME_EXISTS)

        return v

    @root_validator
    def validate_single_name(cls, values):
        name = values.get('name')
        if name:
            existing_services = get_services_list()
            count = existing_services.count(name)
            if count > 1:
                raise ValidationError("Name can only appear once")

        return values

    class Config:
        orm_mode = True