import uuid

import allure
import pytest

from source.api.payments.payment_accounts import get_balance
from source.base.validator import (assert_status_code, assert_json_by_model)
from source.schemas.payments.payment_accounts.payment_accounts_schema import Payments_Accounts


@allure.epic('Payments')
@allure.feature('Payment Accounts')
@allure.story('Balances')
@allure.suite('Tests get balance by uuid')
@pytest.mark.smoke
class TestPaymentsBalancesGet:

    @allure.title('Check balance data of the user')
    @allure.description(f"Проверка успешного ответа [200] при проверке баланса у существующего пользователя")
    def test_positive_valid_user_uuid_get(self):
        response = get_balance(user_uuid="ed841428-dd39-4883-a781-62dd56a9a834")
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Payments_Accounts)

    @allure.title('Check balance of non-existent user')
    @allure.description(f"Проверка ответа [404] при проверке баланса у пользователя с несуществующим {uuid}")
    def test_negative_not_valid_user_uuid_get(self):
        uuid_test = str(uuid.uuid4())  # random uuid
        response = get_balance(user_uuid=uuid_test)
        assert_status_code(response=response, expected=404)