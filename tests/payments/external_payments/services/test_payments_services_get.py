import allure
import pytest

from source.api.payments.payments import get_services_list, create_service, delete_service, get_service
from source.base.validator import (assert_status_code, assert_json_by_model, assert_json_equal_json)
from source.enums.expected import ExpectedJSON
from source.schemas.payments.external_payments_services_schema import External_Payments


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
        assert_json_by_model(response=response, model=External_Payments)
        print(response.text)

    @allure.title('Get non-existent service by id')
    @allure.description('Проверка ответа [404] при запросе несуществующего сервиса оплаты')
    def test_external_payments_services_id_negative_input_non_existent_id_get(self):
        payload = {
            "name": "UNIQ"
        }

        response_1 = create_service(json=payload)
        id_test = response_1.json().get("id")
        assert_json_by_model(response=response_1, model=External_Payments)

        response_2 = delete_service(id_data=id_test)
        assert_status_code(response=response_2, expected=204)

        response_3 = get_service(id_data=id_test)
        assert_status_code(response=response_3, expected=404)
        expected = ExpectedJSON.PAYMENT_SERVICE_NOT_FOUND.value
        assert_json_equal_json(response=response_3, json=expected)

    @allure.title('Get existent service by id')
    @allure.description('Проверка успешного ответа [200] при запросе существующего сервиса оплаты')
    def test_external_payments_services_id_negative_input_non_existent_id_get(self):
        payload = {
            "name": "UNIQ"
        }

        response_1 = create_service(json=payload)
        id_test = response_1.json().get("id")
        assert_status_code(response=response_1, expected=201)

        response_2 = get_service(id_data=id_test)
        assert_status_code(response=response_2, expected=200)
        assert_json_by_model(response=response_2, model=External_Payments)

        response_3 = delete_service(id_data=id_test)
        assert_status_code(response=response_3, expected=204)

    @allure.title(f'Check the response 404 if id is incorrect {1/2}')
    @allure.description(f'Проверка ответа [404] при запросе сервиса оплаты с некорректным id {1/2}')
    def test_services_id_negative_input_non_existent_id_get_1(self):
        response = get_service(id_data="1/2")
        assert_status_code(response=response, expected=404)
        assert "Page not found " in response.text

    @allure.title(f'Check the response 404 if id is incorrect {1,2}')
    @allure.description(f'Проверка ответа [404] при запросе сервиса оплаты с некорректным id {1,2}')
    def test_services_id_negative_input_non_existent_id_get_2(self):
        response = get_service(id_data="1,2")
        assert_status_code(response=response, expected=404)
        expected = ExpectedJSON.PAYMENT_SERVICE_NOT_FOUND.value
        assert_json_equal_json(response=response, json=expected)