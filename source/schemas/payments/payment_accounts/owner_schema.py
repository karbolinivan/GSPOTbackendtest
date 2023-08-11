from typing import Optional
from pydantic import BaseModel, Field, conint, constr, validator, ValidationError
from decimal import Decimal
from source.enums.expected import ExpectedJSON

class PaymentData(BaseModel):

    commission: Optional[constr(regex=r'^(?:100(?:\.00?)?|\d{1,2}(?:\.\d{1,2})?)$')] = Field(None, title='сommission')
    frozen_time: constr(regex=r'^(?:\d+\s)?(?:(\d+):)?(?:\d+):(\d+)(?:\.(\d{1,6}))?$') = Field(..., title='Frozen Time')
    gift_time: constr(regex=r'^(?:\d+\s)?(?:(\d+):)?(?:\d+):(\d+)(?:\.(\d{1,6}))?$') = Field(..., title='Gift Time')
    payout_day_of_month: conint(ge=-2147483648, le=2147483647) = Field(..., title='payout_day_of_month')