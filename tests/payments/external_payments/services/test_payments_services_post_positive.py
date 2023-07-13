import allure
import pytest

from source.api.payments.payments import create_service, delete_service, get_services_list
from source.schemas.payments.external_payments_services_schema import External_Payments
from source.base.validator import (assert_status_code, assert_json_by_model, assert_json_key_value, assert_json_equal_json)


@allure.epic('Payments')
@allure.feature('External Payments')
@allure.story('Services')
@allure.suite('Test post services')
class TestPaymentsPostList:
    @allure.title('Tests of the creating new external payments services')
    @allure.description('Проверка успешного ответа [201] при создании сервиса оплаты с именем {0}')
    @pytest.mark.parametrize("name, expected, message", [
        ("مثال للزخرفة", 201, None),
        ("WeBmAnY", 201, None),
        ("вэб мани", 201, None),
        ("qiwi", 201, None),
        ("fhjthgld3845unfjlcns30567fgcjk", 201, None),
        ("56565", 201, None),
        ("&*^%$", 201, None),
        ("four ", 201, None),
        (" two", 201, None),
        ("bank card", 201, None),
    ])
    def test_external_payments_services_positive_input_value_post(self, name, expected, message):
        response = create_service({"name": name})

        assert_status_code(response=response, expected=expected)
        assert_json_by_model(response=response, model=External_Payments)

        service_id = response.json().get("id")
        if service_id:
            delete_service(service_id)

        print(response.text)



    @allure.title('Tests for deleting external payments services')
    @pytest.mark.parametrize("name", [
        "مثال للزخرفة",
        "WeBmAnY",
        "вэб мани",
        "qiwi",
        "fhjthgld3845unfjlcns30567fgcjk",
        "56565",
        "&*^%$",
        "four ",
        " two",
        "bank card",
    ])
    def test_external_payments_services_delete(self, name):
        # Get the services list
        response = get_services_list()
        assert response.status_code == 200, "Failed to retrieve services list"

        # Find the service ID based on the service name
        services = response.json()
        service_id = None
        for service in services:
            if service["name"] == name:
                service_id = service["id"]
                break

        # Delete the service using the service ID
        assert service_id is not None, f"Failed to find service with name: {name}"
        delete_response = delete_service(service_id)
        assert delete_response.status_code == 200, f"Failed to delete service with name: {name}"
        print(response.text)
        print(123)
