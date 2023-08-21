import allure
import pytest

from source.api.payments.payment_accounts.payout import payout
from source.base.validator import assertions
from source.api.payments.payment_accounts.constants import user_uuid


@allure.epic('Payments')
@allure.feature('Payment Accounts')
@allure.story('Payout')
@allure.suite('Tests patch payout data')
@pytest.mark.smoke
class TestPaymentsPayoutDataPatch:

    @allure.title('Partial update payout data field payout_type use valid value')
    @allure.description(f"Проверка успешного ответа [200] при частичном изменение данных о выплатах поля payout_type используя валидные значения")
    def test_payment_payout_data_positive_input_valid_value_patch(self):
        payload = {
            "account_number": "5566",
            "is_auto_payout": True,
            "payout_type": "yoo_money",
        }
        response = payout.update_payout_data_uuid_partial(json=payload, uuid_data=user_uuid)
        assertions.status_code(actual=response.status_code, expected=200)
        assertions.json_key_value(actual=response.json(), expected=payload, key='payout_type')
        print("Response body: " + response.text)
