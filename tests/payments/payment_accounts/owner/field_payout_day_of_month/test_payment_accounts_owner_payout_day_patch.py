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

    @allure.title('Test payment accounts owner partial update valid value param payout_day_of_month')
    @allure.description(
        'Проверка успешного ответа [200] при частичном обновлении payout_day_of_month валидными значениями')
    @pytest.mark.parametrize("value", [1, 15, 31])
    def test_payment_accounts_owner_positive_input_valid_value_param_payout_day_of_month_patch(self, value):
        """Частичное обновление параметра  payout_day_of_month владельца валидными значениями"""
        print("Запрос PATCH")
        payload = {
            "commission": "10",
            "frozen_time": "10",
            "gift_time": "5",
            "payout_day_of_month": value
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
    @allure.title('Test payment accounts owner partial update invalid value param payout_day_of_month')
    @allure.description('Проверка ответа [400] при частичном обновлении payout_day_of_month невалидными значениями')
    @pytest.mark.parametrize("value", [0, 33, -10, "%$#@", 'twenty', '   ', '1 9', ''])
    def test_payment_accounts_owner_positive_input_invalid_value_param_payout_day_of_month_patch(self, value):
        """Частичное обновление параметра payout_day_of_month владельца невалидными значениями"""
        print("Запрос PATCH")
        payload = {
            "commission": "10",
            "frozen_time": "10",
            "gift_time": "5",
            "payout_day_of_month": value
        }
        response = update_owner_partial(json=payload)
        if isinstance(value, int) and (value < 1 or value > 31):
            pytest.xfail("failing validation actual status code 200, expected status code 400")
        assert_status_code(response=response, expected=400)
        expected = ExpectedJSON.key_value(key="payout_day_of_month",
                                          value=ExpectedJSON.PAYMENT_ACCOUNTS_OWNER_INVALID_VALUE_PAYOUT_DAY.value)
        assert_json_equal_json(response=response, json=expected)
        print("Response body: " + response.text)
