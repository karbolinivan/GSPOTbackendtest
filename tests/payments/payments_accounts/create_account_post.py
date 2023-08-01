import uuid

import allure
import pytest

from source.api.payments.external_payments_services import create_service
from source.api.payments.payment_accounts import increase_balance, delete_balance, get_balance, create_account, \
    delete_payout_data
from source.base.validator import (assert_status_code, assert_json_equal_json, assert_json_by_model)
from source.enums.expected import ExpectedJSON
from source.schemas.payments.payment_accounts.account import Account
from source.schemas.payments.payment_accounts.payment_accounts_schema import Payments_Accounts


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
        print("\n")
        print(response.status_code)
        print(response.text)
        assert_status_code(response=response, expected=201)
        assert_json_by_model(response=response, model=Account)

        # delete is not required according to the test case