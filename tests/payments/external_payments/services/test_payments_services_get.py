import allure
import pytest

from source.api.payments.external_payments_services import get_services_list, delete_service, get_service
from source.base.validator import (assert_status_code, assert_json_by_model, assert_json_equal_json)
from source.enums.expected import ExpectedJSON
from source.schemas.payments.external_payments.services_schema import Payments_Services


@allure.epic('Payments')
@allure.feature('External Payments')
@allure.story('Services')
@allure.suite('Test get services')
@pytest.mark.smoke
class TestPaymentsGetList:

    @allure.title('Test external payments services list')
    @allure.description('Проверка успешного ответа [200] при запросе списка сервисов оплаты')
    def test_external_payments_services_positive_get(self):
        response = get_services_list()
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Payments_Services)
        print(response.text)

    @allure.title('Get non-existent service by id')
    @allure.description('Проверка ответа [404] при запросе несуществующего сервиса оплаты')
    def test_external_payments_services_id_negative_input_non_existent_id_get(self, create_test_payment_service):

        id_test = create_test_payment_service.json().get('id')
        response_1 = delete_service(id_data=id_test)
        assert_status_code(response=response_1, expected=204)

        response_2 = get_service(id_data=id_test)
        assert_status_code(response=response_2, expected=404)
        expected = ExpectedJSON.PAYMENT_SERVICE_NOT_FOUND.value
        assert_json_equal_json(response=response_2, json=expected)

    @allure.title('Get existent service by id')
    @allure.description('Проверка успешного ответа [200] при запросе существующего сервиса оплаты')
    def test_external_payments_services_id_negative_input_non_existent_id_get(self, create_delete_test_payment_service):

        id_test = create_delete_test_payment_service.json().get('id')
        response_2 = get_service(id_data=id_test)
        assert_status_code(response=response_2, expected=200)
        assert_json_by_model(response=response_2, model=Payments_Services)