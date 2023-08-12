import allure
import pytest

from source.api.payments.external_payments_services import create_service
from source.base.validator import (assert_status_code, assert_json_equal_json)
from source.enums.expected import ExpectedJSON


@allure.epic('Payments')
@allure.feature('External Payments')
@allure.story('Services')
@allure.suite('Test post payment services')
@pytest.mark.smoke
class TestPaymentsServicesPostList:

    @allure.title('Check if we can not create the service with an existing name')
    @allure.description(f"Проверка ответа [400] при создании сервиса оплаты с уже существующим именем")
    def test_external_payments_services_negative_create_duplicate_name_post(self, create_delete_test_payment_service):

        name = create_delete_test_payment_service.json().get('name')

        expected = ExpectedJSON.key_value('name', ExpectedJSON.PAYMENT_SERVICE_WITH_THIS_NAME_EXISTS.value)
        response = create_service(json={"name": name})
        assert_status_code(response=response, expected=400)
        assert_json_equal_json(response=response, json=expected)
