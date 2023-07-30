import json
import allure
import pytest

from source.api.payments.payments import create_service, delete_service, get_services_list, get_service
from source.enums.expected import ExpectedJSON
from source.schemas.payments.external_payments_services_schema import External_Payments
from source.base.validator import (assert_status_code, assert_json_by_model, assert_json_key_value,
                                   assert_json_equal_json)


@allure.epic('Payments')
@allure.feature('External Payments')
@allure.story('Services')
@allure.suite('Test put services')
@pytest.mark.smoke
class TestPaymentsPostList:

   pass