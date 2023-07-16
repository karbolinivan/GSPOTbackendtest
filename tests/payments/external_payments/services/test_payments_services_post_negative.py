import allure
import pytest

from source.api.payments.payments import create_service, delete_service
from source.enums.expected import ExpectedJSON
from source.schemas.payments.external_payments_services_schema import External_Payments
from source.base.validator import (assert_status_code, assert_json_by_model, assert_json_key_value, assert_json_equal_json)


@allure.epic('Payments')
@allure.feature('External Payments')
@allure.story('Services')
@allure.suite('Test post services')
class TestPaymentsPostList:

    @allure.title('Tests of the creating new external payments services')
    @allure.description(f"Проверка ответа [400] при создании сервиса оплаты с некорректным именем {0}")
    @pytest.mark.parametrize("name, expected, message", [
    ])
    def test_external_payments_services_negative_input_value_post(self, name, expected, message):
        response = create_service({"name": name})

        print(f"Response: {response.json()}")

        assert_status_code(response=response, expected=expected)
        assert_json_by_model(response=response, model=External_Payments)

        print(response.json())
        print(123)

        service_id = response.json()["id"]
        delete_service(service_id)
        
        print(response.text)


    @allure.title('Tests of creating new external payments services')
    @allure.description('Check unsuccessful response [400] when creating a payment service with an empty body')
    def test_external_payments_services_empty_body_post(self):
        response = create_service({})

        assert_status_code(response=response, expected=400)
        assert_json_by_model(response=response, model=External_Payments)

        service_id = response.json()["id"]
        delete_service(service_id)

        print(response.text)

    @allure.title('Tests of creating new external payments services')
    @allure.description('Check unsuccessful response [400] when creating a payment service with two different names')
    def test_external_payments_services_two_names_post(self):
        names = ["service1", "service2"]
        responses = []

        for name in names:
            json_body = {"name": name}
            response = create_service(json_body)

            assert_status_code(response=response, expected=400)
            assert_json_by_model(response=response, model=External_Payments)

            responses.append(response)

        for response in responses:
            service_id = response.json()["id"]
            delete_service(service_id)

        print(responses)