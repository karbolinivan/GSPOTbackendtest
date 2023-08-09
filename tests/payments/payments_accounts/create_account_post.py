import uuid

import allure
import pytest

from source.api.payments.payment_accounts import create_account
from source.base.validator import (assert_status_code, assert_json_by_model)
from source.schemas.payments.payment_accounts.account import Account


@allure.epic('Payments')
@allure.feature('Payment Accounts')
@allure.story('Create Account')
@allure.suite('Tests create account')
@pytest.mark.smoke
class TestCreateAccountPost:

    @allure.title('Check of creation of a new account')
    @allure.description(f"Проверка успешного ответа [200] при создании аккаунта с новым {uuid}")
    def test_payment_accounts_create_account_positive_valid_uuid_post(self):

        uuid_test = str(uuid.uuid4()) # random uuid
        response = create_account(json={"user_uuid":uuid_test})

        assert_status_code(response=response, expected=201)
        assert_json_by_model(response=response, model=Account)