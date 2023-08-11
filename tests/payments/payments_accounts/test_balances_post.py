import uuid

import allure
import pytest

from source.api.payments.payment_accounts import post_balance, create_account
from source.base.validator import (assert_json_by_model, assert_status_code)
from source.schemas.payments.payment_accounts.account import Account
from source.schemas.payments.payment_accounts.payment_accounts_schema import Payments_Accounts


@allure.epic('Payments')
@allure.feature('Payment Accounts')
@allure.story('Balances')
@allure.suite('Tests post balance')
@pytest.mark.smoke
class TestBalancesPostList:

    @allure.title('Check balance data of the user')
    @allure.description(f"Проверка успешного ответа [200] при получении информации о балансе у имеющегося юзера")
    def test_balances_positive_post(self):
        payload = {
            "uuid_list": [
                "3fa85f64-5717-4562-b3fc-2c963f66afa6"
            ]
        }

        response = post_balance(json=payload)

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
        response2 = post_balance(json=payload)
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

        # POST
        payload = {
            "uuid_list": [
                uuid_test_1, uuid_test_2
            ]
        }
        response = post_balance(json=payload)
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Payments_Accounts)

    @allure.title('Check balance data of user with invalid uuid')
    @allure.description(f"Проверка ответа [400] при получении информации о балансе у юзера с невалидным {uuid}")
    def test_balances_negative_invalid_uuid_post(self):
        payload = {
            "uuid_list": [
                "3fa85f64-5717-4562-b3fc-2c963f66afa"
            ]
        }
        response = post_balance(json=payload)
        expected = {"uuid_list": {"0": ["Must be a valid UUID."]}}
        assert_status_code(response=response, expected=400)
        assert (response.text, expected)

    @allure.title('Check balance data of non-existent user')
    @allure.description(f"Проверка ответа [400] при получении информации о балансе у несуществующего юзера")
    def test_balances_negative_enter_non_existent_uuid_post(self):
        payload = {
            "uuid_list": [
                "aaf5f6b2-d595-486a-8e51-108d3b175445"
            ]
        }
        response = post_balance(json=payload)
        expected = {
            "detail": "Field user_uuid with next values {UUID('aaf5f6b2-d595-486a-8e51-108d3b175445')} not found in database."}
        assert_status_code(response=response, expected=404)
        assert (response.text, expected)

    @allure.title('Check balance data of user with empty uuid')
    @allure.description(f"Проверка ответа [400] при получении информации о балансе у юзера с пустым {uuid}")
    def test_balances_negative_empty_uuid_field_post(self):
        payload = {
            "uuid_list": []
        }
        response = post_balance(json=payload)
        assert_status_code(response=response, expected=400) # BUG !!!
