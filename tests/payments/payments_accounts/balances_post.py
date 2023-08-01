import uuid

import allure
import pytest

from source.api.payments.external_payments_services import create_service
from source.api.payments.payment_accounts import increase_balance, delete_balance, get_balance
from source.base.validator import (assert_status_code, assert_json_equal_json)
from source.enums.expected import ExpectedJSON


@allure.epic('Payments')
@allure.feature('Payment Accounts')
@allure.story('Balances')
@allure.suite('Tests post balance')
@pytest.mark.smoke
class TestPaymentsPostList:

    @allure.title('Check balance data of the user')
    @allure.description(f"Проверка успешного ответа [200] при создании сервиса оплаты с уже существующим именем")
    def test_get(self):
        response = get_balance(user_uuid="3fa85f64-5717-4562-b3fc-2c963f66afa6") #should be post
        print("\n")
        print(response.status_code)
        print(response.text)

        test_uuid = str(uuid.uuid4())
        response = get_balance(user_uuid=test_uuid)