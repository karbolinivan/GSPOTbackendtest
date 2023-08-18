import allure
import pytest

from source.api.payments.payment_accounts.payout import payout
from source.base.validator import assertions
from source.enums.expected import ExpectedJSON
from source.api.payments.payment_accounts.constants import user_uuid
from source.schemas.payments.payment_accounts.payout_data_schema import PayoutData


@allure.epic('Payments')
@allure.feature('Payment Accounts')
@allure.story('Payout')
@allure.suite('Tests post payout data')
@pytest.mark.smoke
class TestPaymentsPayoutDataPost:

    @allure.title('Create payout data use valid value')
    @allure.description(f"Проверка успешного ответа [200] при создании данных о выплатах используя валидные значения")
    def test_payment_payout_data_positive_input_valid_value_post(self):
        payload = {
            "account_number": "55gg66",
            "is_auto_payout": True,
            "payout_type": "bank_card",
            "user_uuid": user_uuid
        }
        response = payout.create_payout_data(json=payload)
        assertions.status_code(actual=response.status_code, expected=201)
        assertions.json_by_model(actual=response.json(), model=PayoutData)
        print("Response body: " + response.text)


@allure.epic('Payments')
@allure.feature('Payment Accounts')
@allure.story('Payout')
@allure.suite('Tests post payout data regression')
@pytest.mark.regression
class TestPaymentsPayoutDataPostRegression:

    @allure.title('Create payout data use invalid value fields account_number and payout_type')
    @allure.description(f"Проверка ответа [400] при создании данных о выплатах используя невалидные значения")
    @pytest.mark.parametrize("value1, value2", [("55hhgg66", "paypal"), ("fdgfhfhd", "yoo_money")])
    def test_payment_payout_data_negative_input_invalid_value_post(self, value1, value2):
        payload = {
            "account_number": f'{value1}',
            "is_auto_payout": True,
            "payout_type": f'{value2}',
            "user_uuid": user_uuid
        }
        response = payout.create_payout_data(json=payload)
        if value2 == "paypal":
            expected = ExpectedJSON.key_value(key="payout_type", value=ExpectedJSON.PAYMENT_ACCOUNTS_PAYOUT_DATA_INVALID_VALUE_PAYOUT_TYPE.value)
            assertions.status_code(actual=response.status_code, expected=400)
            assertions.json_equal_json(actual=response.json(), expected=expected)
        elif value2 == "yoo_money" and value1.isalpha():
            expected = ExpectedJSON.key_value(key="account_number", value=ExpectedJSON.PAYMENT_ACCOUNTS_PAYOUT_DATA_INVALID_VALUE_ACCOUNT_NUMBER_YOO_MONEY.value)
            assertions.status_code(actual=response.status_code, expected=400)
            assertions.json_equal_json(actual=response.json(), expected=expected)
        print("Response body: " + response.text)
