import allure
import pytest

from source.api.payments.payment_accounts.owner import update_owner_partial
from source.base.validator import assert_status_code, assert_json_equal_json, assert_json_by_model
from source.enums.expected import ExpectedJSON
from source.schemas.payments.payment_accounts.owner_schema import PaymentData

@allure.epic('Payments')
@allure.feature('Payment accounts')
@allure.story('Owner')
@allure.suite('Test patch owners')
@pytest.mark.smoke

class TestPaymentPatchOwner:

    @allure.title('Test payment accounts owner partial update valid value param gift_time')
    @allure.description('Проверка успешного ответа [200] при частичном обновлении gift_time валидными значениями')
    @pytest.mark.parametrize("value", ["0", "11:25:45", "1", "12 11:05:33.666666"])
    def test_payment_accounts_owner_positive_input_valid_value_param_gift_time_patch(self, value):
        """Частичное обновление параметра  gift_time владельца валидными значениями"""
        print("Запрос PATCH")
        payload = {
            "commission": "08",
            "frozen_time": "12:15:44",
            "gift_time": f'{value}',
            "payout_day_of_month": 4
        }
        response = update_owner_partial(json=payload)
        assert_json_by_model(response=response, model=PaymentData)
        assert_status_code(response=response, expected=200)
        print("Response body: " + response.text)

@allure.epic('Payments')
@allure.feature('Payment accounts')
@allure.story('Owner')
@allure.suite('Test patch owners regression')
@pytest.mark.regression

class TestPaymentPatchOwnerRegression:
    @allure.title('Test payment accounts owner partial update invalid value param gift_time')
    @allure.description('Проверка ответа [400] при частичном обновлении gift_time невалидными значениями')
    @pytest.mark.parametrize("value", ["12 11:05:33.6666555765553", "%$!@#@", "frozen","", "   ", "11:2 5:45", "  11:25:45", "11:25:45  "])
    def test_payment_accounts_owner_positive_input_invalid_value_param_gift_time_patch(self, value):
        """Частичное обновление параметра gift_time владельца невалидными значениями"""
        print("Запрос PATCH")
        payload = {
            "commission": "10",
            "frozen_time": "12:15:44",
            "gift_time": f'{value}',
            "payout_day_of_month": 4
        }
        response = update_owner_partial(json=payload)
        if isinstance(value, str) and value == "":
            pytest.xfail("failing validation actual status code 200, expected status code 400")
        expected = ExpectedJSON.key_value(key="gift_time", value=ExpectedJSON.PAYMENT_ACCOUNTS_OWNER_INVALID_VALUE_GIFT_TIME.value)
        assert_json_equal_json(response=response, json=expected)
        assert_status_code(response=response, expected=400)
        print("Response body: " + response.text)
