import allure
import pytest

from source.api.payments.payment_accounts.owner import update_owner
from source.base.validator import assert_status_code, assert_json_equal_json, assert_json_by_model
from source.enums.expected import ExpectedJSON
from source.schemas.payments.payment_accounts.owner_schema import PaymentData

@allure.epic('Payments')
@allure.feature('Payment accounts')
@allure.story('Owner')
@allure.suite('Test put owners')
@pytest.mark.smoke

class TestPaymentPutOwner:

    @allure.title('Test payment accounts owner update valid value param frozen_time')
    @allure.description('Проверка успешного ответа [200] при изменении frozen_time владельца валидными значениями')
    @pytest.mark.parametrize("value", ["0", "11:25:45", "1", "12 11:05:33.666666"])
    def test_payment_accounts_owner_positive_input_valid_value_param_frozen_time_put(self, value):
        """Изменение параметра  frozen_time владельца валидными значениями"""
        print("Запрос PUT")
        payload = {
            "commission": "08",
            "frozen_time": f'{value}',
            "gift_time": "5",
            "payout_day_of_month": 4
        }
        response = update_owner(json=payload)
        assert_json_by_model(response=response, model=PaymentData)
        assert_status_code(response=response, expected=200)
        print("Response body: " + response.text)

@allure.epic('Payments')
@allure.feature('Payment accounts')
@allure.story('Owner')
@allure.suite('Test put owners regression')
@pytest.mark.regression

class TestPaymentPutOwnerRegression:
    @allure.title('Test payment accounts owner update invalid value param frozen_time')
    @allure.description('Проверка ответа [400] при изменении frozen_time владельца невалидными значениями')
    @pytest.mark.parametrize("value", ["12 11:05:33.6666555765553", "%$!@#@", "frozen","", "   ", "11:2 5:45", "  11:25:45", "11:25:45  "])
    def test_payment_accounts_owner_positive_input_invalid_value_param_frozen_time_put(self, value):
        """Изменение параметра frozen_time владельца невалидными значениями"""
        print("Запрос PUT")
        payload = {
            "commission": "10",
            "frozen_time": f'{value}',
            "gift_time": "5",
            "payout_day_of_month": 4
        }
        response = update_owner(json=payload)
        if isinstance(value, str) and value == "":
            pytest.xfail("failing validation actual status code 200, expected status code 400")
        expected = ExpectedJSON.key_value(key="frozen_time", value=ExpectedJSON.PAYMENT_ACCOUNTS_OWNER_INVALID_VALUE_FROZEN_TIME.value)
        assert_json_equal_json(response=response, json=expected)
        assert_status_code(response=response, expected=400)
        print("Response body: " + response.text)
