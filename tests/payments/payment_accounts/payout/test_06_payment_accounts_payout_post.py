import allure
import pytest

from source.api.payments.payment_accounts.payout import payout
from source.base.validator import assertions
from source.api.payments.payment_accounts.constants import user_uuid
from source.enums.expected import ExpectedJSON


@allure.epic('Payments')
@allure.feature('Payment Accounts')
@allure.story('Payout')
@allure.suite('Tests post payout')
@pytest.mark.smoke
class TestPaymentsPayoutPost:

    @allure.title('Create payout use valid value but no available balance ')
    @allure.description(f"Проверка ответа [400] при создании данных о выплатах используя валидные данные без доступного баланса")
    def test_payment_payout_positive_input_valid_value_post(self, update_test_payment_owner_payout_day):
        payload = {
            "amount": {
                "value": 500000,
                "currency": "RUB"
            },
            "payout_destination_data": {
                "type_": "BANK_CARD",
                "account_number": "456456"
            },
            "user_uuid": user_uuid
        }
        response = payout.create_payout(json=payload)
        assertions.status_code(actual=response.status_code, expected=400)
        expected = ExpectedJSON.key_value(key="error", value=ExpectedJSON.PAYMENT_ACCOUNTS_PAYOUT_NO_AVAILABLE_BALANCE.value)
        assertions.json_equal_json(actual=response.json(), expected=expected)
        print("Response body: " + response.text)

