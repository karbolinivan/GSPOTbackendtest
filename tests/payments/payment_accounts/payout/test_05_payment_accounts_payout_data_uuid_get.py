import allure
import pytest

from source.api.payments.payment_accounts.payout import payout
from source.base.validator import assertions


@allure.epic('Payments')
@allure.feature('Payment Accounts')
@allure.story('Payout')
@allure.suite('Tests get payout data uuid')
@pytest.mark.smoke
class TestPaymentsPayoutDataGet:

    @allure.title('Check payout data of the user')
    @allure.description(f"Проверка успешного ответа [200] при выводе данных о выплатах у существующего пользователя")
    def test_payment_payout_data_positive_valid_user_uuid_get(self, create_delete_test_payment_payout_data):
        id_test = create_delete_test_payment_payout_data.json().get("user_uuid")
        response = payout.get_payout_data_uuid(uuid_data=id_test)
        assertions.status_code(actual=response.status_code, expected=200)
        print("Response body: " + response.text)
