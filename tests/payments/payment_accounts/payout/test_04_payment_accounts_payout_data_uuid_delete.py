import allure
import pytest

from source.api.payments.payment_accounts.payout import payout
from source.base.validator import assertions
from source.api.payments.payment_accounts.constants import user_uuid


@allure.epic('Payments')
@allure.feature('Payment Accounts')
@allure.story('Payout')
@allure.suite('Tests delete payout data')
@pytest.mark.smoke
class TestPaymentsPayoutDataDelete:

    @allure.title('Delete payout data of the user')
    @allure.description(f"Проверка успешного ответа [200] при удалении данных о выплатах у существующего пользователя")
    def test_payment_payout_data_positive_valid_user_uuid_delete(self):
        response = payout.delete_payout_data_uuid(uuid_data=user_uuid)
        assertions.status_code(actual=response.status_code, expected=204)
