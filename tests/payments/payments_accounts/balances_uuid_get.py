import allure
import pytest

from source.api.payments.external_payments_services import create_service
from source.api.payments.payment_accounts import increase_balance, delete_balance, get_balance
from source.base.validator import (assert_status_code, assert_json_equal_json, assert_json_by_model)
from source.enums.expected import ExpectedJSON
from source.schemas.payments.payment_accounts.payment_accounts_schema import Payments_Accounts


@allure.epic('Payments')
@allure.feature('Payment Accounts')
@allure.story('Balances')
@allure.suite('Tests post balance')
@pytest.mark.smoke
class TestPaymentsPostList:

    @allure.title('Check balance data of the user')
    @allure.description(f"Проверка успешного ответа [200] при создании сервиса оплаты с уже существующим именем")
    def test_positive_valid_user_uuid_get(self):
        response = get_balance(user_uuid="ed841428-dd39-4883-a781-62dd56a9a834") #should be post
        print("\n")
        print(response.status_code)
        print(response.text)
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Payments_Accounts)