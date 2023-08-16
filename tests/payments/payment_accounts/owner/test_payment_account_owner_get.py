import allure
import pytest

from source.api.payments.payment_accounts.owner import get_owner_list
from source.base.validator import assert_status_code

@allure.epic('Payments')
@allure.feature('Payment accounts')
@allure.story('Owner')
@allure.suite('Test get owners')
@pytest.mark.smoke

class TestPaymentGetList:

    @allure.title('Test payment accounts owner list')
    @allure.description('Проверка успешного ответа [200] при запросе списка владельцев')
    def test_payment_accounts_owner_positive_get(self):
        """Вывод списка владельцев"""
        print("Запрос Get")
        response = get_owner_list()
        assert_status_code(response=response, expected=200)
        print("Response body: " + response.text)
