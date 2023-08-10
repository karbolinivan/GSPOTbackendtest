import uuid

import allure
import pytest

from source.api.payments.payment_accounts import increase_balance
from source.base.validator import (assert_status_code, assert_json_by_model)
from source.schemas.payments.payment_accounts.increase_balance_schema import Increase_Balance


@allure.epic('Payments')
@allure.feature('Payment Accounts')
@allure.story('Balances')
@allure.suite('Tests increase balance')
@pytest.mark.smoke
class TestPaymentsPostList:

    @allure.title('Check if we can not create the service with an existing name')
    @allure.description(f"Проверка ответа [400] при создании сервиса оплаты с уже существующим именем")
    @pytest.mark.xfail(reason="https://trello.com/c/5JhiBEV8")
    def test_positive_increase_balance_post(self):
        uuid_test = str(uuid.uuid4())  # random uuid
        payload = {
            "payment_type": "bank_card",
            "payment_service": "yookassa",
            "payment_amount": 999999999,
            "user_uuid": uuid_test,
            "return_url": "string"
        }
        response = increase_balance(json=payload)

        assert_status_code(response=response, expected=201)
        assert_json_by_model(response=response, model=Increase_Balance)

    @allure.title('Check if we can not create the service with an existing name')
    @allure.description(f"Проверка ответа [400] при создании сервиса оплаты с уже существующим именем")
    @pytest.mark.xfail(reason="https://trello.com/c/5JhiBEV8")
    def test_negative_increase_balance_post(self):
        uuid_test = str(uuid.uuid4())  # random uuid
        payload = {
            "payment_type": "bank_card",
            "payment_service": "yookassa",
            "payment_amount": -1,
            "user_uuid": uuid_test,
            "return_url": "string"
        }
        response = increase_balance(json=payload)
        expected = {"payment_amount": ["Insufficient Funds"]}
        print(response.text)
        assert_status_code(response=response, expected=400)
        assert response.text == expected



