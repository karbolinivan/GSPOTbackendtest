import uuid

import allure
import pytest

from source.api.payments.payment_accounts.create_account import create_account
from source.base.validator import (assert_status_code, assert_json_by_model)
from source.schemas.payments.payment_accounts.account import Account


@allure.epic('Payments')
@allure.feature('Payment Accounts')
@allure.story('Create Account')
@allure.suite('Tests create account post')
@pytest.mark.smoke
class TestCreateAccountPost:

    @allure.title('Check of creation of a new account')
    @allure.description(f"Проверка успешного ответа [200] при создании аккаунта с новым {uuid}")
    def test_payment_accounts_create_account_positive_valid_uuid_post(self):
        uuid_test = str(uuid.uuid4())  # random uuid
        response = create_account(json={"user_uuid": uuid_test})

        assert_status_code(response=response, expected=201)
        assert_json_by_model(response=response, model=Account)

    @allure.title('Check of creation account with an existing uuid')
    @allure.description(f"Проверка ответа [409] при попытке создания аккаунта с существующим {uuid}")
    def test_payment_accounts_create_account_negative_existing_uuid_post(self):
        uuid_test = str(uuid.uuid4())  # random uuid
        response = create_account(json={"user_uuid": uuid_test})
        assert_status_code(response=response, expected=201)
        assert_json_by_model(response=response, model=Account)

        response2 = create_account(json={"user_uuid": uuid_test})
        assert_status_code(response=response2, expected=409)
        assert (response.text, {"error": "A user with this UUID already exists"})

    @allure.title('Check of creation account with invalid uuid')
    @allure.description(f"Проверка ответа [409] при попытке создания аккаунта с невалидным {uuid}")
    @pytest.mark.skip(reason="passed in swagger, needs to be rechecked")
    def test_negative_more_characters_post(self):
        payload = {
            "user_uuid": "ed4b42d6-45f0-471c-88bc-0571270fb3741"
        }
        response = create_account(json=payload)
        assert_status_code(response=response, expected=500)
        assert (response.text, "['“ed4b42d6-45f0-471c-88bc-0571270fb3741” is not a valid UUID.']")

    @allure.title('Check of creation account with invalid uuid')
    @allure.description(f"Проверка ответа [409] при попытке создания аккаунта с невалидным {uuid}")
    @pytest.mark.skip(reason="passed in swagger, needs to be rechecked")
    def test_negative_less_characters_post(self):
        payload = {
            "user_uuid": "ed4b42d6-45f0-471c-88bc-0571270fb37"
        }
        response = create_account(json=payload)
        assert_status_code(response=response, expected=500)
        assert (response.text, "['“ed4b42d6-45f0-471c-88bc-0571270fb37” is not a valid UUID.']")
