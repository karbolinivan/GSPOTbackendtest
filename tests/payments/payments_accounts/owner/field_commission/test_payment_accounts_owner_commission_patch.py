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

    @allure.title('Test payment accounts owner partial update valid value param commission')
    @allure.description('Проверка успешного ответа [200] при частичном обновлении commission валидными значениями')
    @pytest.mark.parametrize("value", ["0", "50", "100", "5.5", "1.22", ""])
    def test_payment_accounts_owner_positive_input_valid_value_param_commission_patch(self, value):
        """Частичное обновление commission владельца валидными значениями"""
        print("Запрос PATCH")
        payload = {
            "commission": f'{value}',
            "frozen_time": "10",
            "gift_time": "5",
            "payout_day_of_month": 4
        }
        response = update_owner_partial(json=payload)
        if isinstance(value, str) and value == "":
            print("expected status code 200")
            pytest.xfail("failing validation actual status code 400, expected status code 200")
        assert_json_by_model(response=response, model=PaymentData)
        assert_status_code(response=response, expected=200)
        print("Response body: " + response.text)


@allure.epic('Payments')
@allure.feature('Payment accounts')
@allure.story('Owner')
@allure.suite('Test patch owners regression')
@pytest.mark.regression
class TestPaymentPatchOwnerRegression:
    @allure.title('Test payment accounts owner partial update invalid value param commission')
    @allure.description('Проверка ответа [400] при частичном обновлении commission невалидными значениями')
    @pytest.mark.parametrize("value", ["100.000", "-20", "101", "1.225", "%$#@", "fifty", "5 0", "   "])
    def test_payment_accounts_owner_positive_input_invalid_value_param_commission_patch(self, value):
        """Частичное обновление commission владельца невалидными значениями"""
        print("Запрос PATCH")
        payload = {
            "commission": f'{value}',
            "frozen_time": "10",
            "gift_time": "5",
            "payout_day_of_month": 4
        }
        response = update_owner_partial(json=payload)
        if isinstance(value, str) and value == "100.000":
            expected = ExpectedJSON.key_value(key="commission",
                                              value=ExpectedJSON.PAYMENT_ACCOUNTS_OWNER_MORE_THAN_5_DIGITS_IN_TOTAL_COMMISSION.value)
        elif isinstance(value, str) and value == "-20":
            expected = ExpectedJSON.key_value(key="commission",
                                              value=ExpectedJSON.PAYMENT_ACCOUNTS_OWNER_LESS_THAN_ALLOWED_COMMISSION.value)
        elif isinstance(value, str) and value == "101":
            expected = ExpectedJSON.key_value(key="commission",
                                              value=ExpectedJSON.PAYMENT_ACCOUNTS_OWNER_EXCEEDED_LENGTH_COMMISSION.value)
        elif isinstance(value, str) and value == "1.225":
            expected = ExpectedJSON.key_value(key="commission",
                                              value=ExpectedJSON.PAYMENT_ACCOUNTS_OWNER_MORE_THAN_2_DECIMAL_PLACES_COMMISSION.value)
        else:
            expected = ExpectedJSON.key_value(key="commission",
                                              value=ExpectedJSON.PAYMENT_ACCOUNTS_OWNER_INVALID_VALUE_COMMISSION.value)

        assert_json_equal_json(response=response, json=expected)
        assert_status_code(response=response, expected=400)
        print("Response body: " + response.text)
