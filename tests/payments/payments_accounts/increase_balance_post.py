import allure
import pytest

from source.api.payments.external_payments_services import create_service
from source.api.payments.payment_accounts import increase_balance, delete_balance, get_balance
from source.base.validator import (assert_status_code, assert_json_equal_json)
from source.enums.expected import ExpectedJSON


@allure.epic('Payments')
@allure.feature('Payment Accounts')
@allure.story('Balances')
@allure.suite('Tests increase balance')
@pytest.mark.smoke
class TestPaymentsPostList:

    @allure.title('Check if we can not create the service with an existing name')
    @allure.description(f"Проверка ответа [400] при создании сервиса оплаты с уже существующим именем")
    def test_positive_increase_balance_post(self):
        payload = {
            "payment_type": "bank_card",
            "payment_service": "yookassa",
            "payment_amount": 999999999,
            "user_uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "return_url": "string"
        }
        response = increase_balance(json=payload)
        test_id = response.json().get('id')
        responce2 = delete_balance(id_data=test_id)




