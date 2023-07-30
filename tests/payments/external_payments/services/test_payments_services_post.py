import allure
import allure
import pytest

from source.api.payments.payments import create_service, delete_service, get_service
from source.base.validator import (assert_status_code, assert_json_by_model, assert_json_key_value,
                                   assert_json_equal_json)
from source.enums.expected import ExpectedJSON
from source.schemas.payments.external_payments_services_schema import External_Payments


@allure.epic('Payments')
@allure.feature('External Payments')
@allure.story('Services')
@allure.suite('Test post services')
@pytest.mark.smoke
class TestPaymentsPostList:

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