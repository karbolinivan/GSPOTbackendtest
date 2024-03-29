import allure
import pytest

from source.api.payments.external_payments_services import delete_service
from source.base.validator import (assert_status_code, assert_json_equal_json)
from source.enums.expected import ExpectedJSON


@allure.epic('Payments')
@allure.feature('External Payments')
@allure.story('Services')
@allure.suite('Test delete payment services')
@pytest.mark.smoke
class TestPaymentsServicesDelete:

    @allure.title('Test of deleting non-existent service by id')
    @allure.description('Проверка ответа [404] при удалении по id несуществующего сервиса оплаты')
    def test_external_payments_services_id_negative_remove_non_existent_service_delete(self, create_test_payment_service):

        id_test = create_test_payment_service.json().get('id')
        response_1 = delete_service(id_data=id_test)
        assert_status_code(response=response_1, expected=204)

        response_2 = delete_service(id_data=id_test)
        expected = ExpectedJSON.PAYMENT_SERVICE_NOT_FOUND.value
        assert_json_equal_json(response=response_2, json=expected)
        assert_status_code(response=response_2, expected=404)

    @allure.title('Test of successful deleting existent service by id')
    @allure.description('Проверка успешного ответа [204] при удалении по id существующего сервиса оплаты')
    def test_external_payments_services_id_positive_delete(self, create_test_payment_service):

        id_test = create_test_payment_service.json().get('id')
        response_2 = delete_service(id_data=id_test)
        assert_status_code(response=response_2, expected=204)

    @allure.title(f'Check the response 404 while deleting multiple services {1/2}')
    @allure.description(f'Проверка ответа [404] при удалении нескольких сервисов оплаты {1/2}')
    @pytest.mark.xfail(reason="Response text is too long (should be only error message)")
    def test_external_payments_services_id_negative_remove_multiple_services_delete_1(self):
        response = delete_service(id_data="1/2")
        assert_status_code(response=response, expected=404)
        expected = ExpectedJSON.PAYMENT_SERVICE_NOT_FOUND.value
        assert_json_equal_json(response=response, json=expected)

    @allure.title(f'Check the response 404 while deleting multiple services {1,2}')
    @allure.description(f'Проверка ответа [404] при удалении нескольких сервисов оплаты {1,2}')
    def test_external_payments_services_id_negative_remove_multiple_services_delete_2(self):
        response = delete_service(id_data="1,2")
        assert_status_code(response=response, expected=404)
        expected = ExpectedJSON.PAYMENT_SERVICE_NOT_FOUND.value
        assert_json_equal_json(response=response, json=expected)