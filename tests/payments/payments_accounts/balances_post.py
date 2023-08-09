import uuid

import allure
import pytest
import requests

from source.api.payments.payment_accounts import get_balance, create_balance, create_account
from source.base.validator import (assert_json_by_model, assert_status_code)
from source.schemas.payments.payment_accounts.account import Account
from source.schemas.payments.payment_accounts.payment_accounts_schema import Payments_Accounts


@allure.epic('Payments')
@allure.feature('Payment Accounts')
@allure.story('Balances')
@allure.suite('Tests post balance')
@pytest.mark.smoke
class TestPaymentsPostList:

    @allure.title('Check balance data of the user')
    @allure.description(f"Проверка успешного ответа [200] при получении информации о балансе у имеющегося юзера")
    def test_balances_positive_post(self):
        payload = {
            "uuid_list": [
                "3fa85f64-5717-4562-b3fc-2c963f66afa6"
            ]
        }

        response = create_balance(json=payload)

        print(response.status_code)
        print(response.text)

        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Payments_Accounts)

    @allure.title('Check balance data of the user')
    @allure.description(f"Проверка успешного ответа [200] при получении информации о балансе у имеющегося юзера")
    def test_balances_positive_new_uuid_post(self):
        # CREATE ACCOUNT
        uuid_test = str(uuid.uuid4())  # random uuid
        response = create_account(json={"user_uuid": uuid_test})
        assert_status_code(response=response, expected=201)
        assert_json_by_model(response=response, model=Account)

        # POST
        test_id = response.json().get('user_uuid')
        payload = {
            "uuid_list": [
                test_id
            ]
        }
        response2 = create_balance(json=payload)
        assert_status_code(response=response2, expected=200)
        assert_json_by_model(response=response2, model=Payments_Accounts)


    @allure.title('Check balance data of the user')
    @allure.description(f"Проверка успешного ответа [200] при получении информации о балансе у имеющегося юзера")
    def test_balances_positive_multiple_uuids_post(self):

        # CREATE TWO ACCOUNTS
        uuid_test_1 = str(uuid.uuid4())  # random uuid
        uuid_test_2 = str(uuid.uuid4())  # random uuid

        response = create_account(json={"user_uuid": uuid_test_1})
        assert_status_code(response=response, expected=201)
        assert_json_by_model(response=response, model=Account)

        response2 = create_account(json={"user_uuid": uuid_test_2})
        assert_status_code(response=response2, expected=201)
        assert_json_by_model(response=response2, model=Account)

        test_id_1 = response.json().get('user_uuid')
        test_id_2 = response2.json().get('user_uuid')

        # POST
        payload = {
            "uuid_list": [
                test_id_1, test_id_2
            ]
        }
        response = create_balance(json=payload)
        print(response.status_code)
        print(response.text)
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Payments_Accounts)


