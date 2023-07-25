import json
import allure
import pytest

from source.api.payments.payments import create_service, delete_service, get_services_list, get_service
from source.enums.expected import ExpectedJSON
from source.schemas.payments.external_payments_services_schema import External_Payments
from source.base.validator import (assert_status_code, assert_json_by_model, assert_json_key_value,
                                   assert_json_equal_json)


@allure.epic('Payments')
@allure.feature('External Payments')
@allure.story('Services')
@allure.suite('Test post services')
class TestPaymentsPostList:

    @allure.title('Tests of the creating new external payments services')
    @allure.description(f"Проверка успешного ответа [201] при создании сервиса оплаты с именем {0}")
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
        # Cleaning the database (optional)
        response = get_services_list()
        parsed_data = json.loads(response.text)
        for item in parsed_data:
            service_id = item['id']
            r = delete_service(service_id)
            print(f"Deleted service with ID {service_id}. Status code: {r.status_code}")

        # Creating new data
        response = create_service({"name": name})
        assert_status_code(response=response, expected=expected)
        assert_json_by_model(response=response, model=External_Payments)

        # Deleting created data
        service_id = response.json().get("id")
        if service_id:
            delete_response = delete_service(service_id)
            assert delete_response.status_code == 204, "Unable to delete"


    @allure.title('Check if we can not create the service with an existing name')
    @allure.description(f"Проверка ответа [400] при создании сервиса оплаты с уже существующим именем")
    def test_external_payments_services_negative_create_duplicate_name_post(self):
        payload = {
            "name": "UNIQ"
        }

        response_1 = create_service(json=payload)
        id_test_1 = response_1.json().get("id")
        assert_status_code(response=response_1, expected=201)
        assert_json_by_model(response=response_1, model=External_Payments)
        assert_json_key_value(response=response_1, json=payload, key='name')

        expected_1 = ExpectedJSON.key_value('name', ExpectedJSON.PAYMENT_SERVICE_WITH_THIS_NAME_EXISTS.value)
        response_2 = create_service(json=payload)
        assert_status_code(response=response_2, expected=400)
        assert_json_equal_json(response=response_2, json=expected_1)

        response_3 = delete_service(id_data=id_test_1)
        assert_status_code(response=response_3, expected=204)

        expected_2 = ExpectedJSON.PAYMENT_SERVICE_NOT_FOUND.value
        response_4 = get_service(id_data=id_test_1)
        assert_status_code(response=response_4, expected=404)
        assert_json_equal_json(response=response_4, json=expected_2)