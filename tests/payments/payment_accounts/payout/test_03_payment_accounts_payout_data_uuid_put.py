import allure
import pytest

from source.api.payments.payment_accounts.payout import payout
from source.base.validator import assertions
from source.api.payments.payment_accounts.constants import user_uuid


@allure.epic('Payments')
@allure.feature('Payment Accounts')
@allure.story('Payout')
@allure.suite('Tests put payout data')
@pytest.mark.smoke
class TestPaymentsPayoutDataPut:

    @allure.title('Update payout data field payout_type use valid value')
    @allure.description(f"Проверка успешного ответа [200] при изменение данных о выплатах поля payout_type используя валидные значения")
    @pytest.mark.parametrize("value", ["yoo_money", "bank_card"])
    def test_payment_payout_data_positive_input_valid_value_put(self, value):
        payload = {
            "account_number": "5566",
            "is_auto_payout": True,
            "payout_type": f'{value}',
        }
        response = payout.update_payout_data_uuid(json=payload, uuid_data=user_uuid)
        assertions.status_code(actual=response.status_code, expected=200)
        assertions.json_key_value(actual=response.json(), expected=payload, key='payout_type')
        print("Response body: " + response.text)
