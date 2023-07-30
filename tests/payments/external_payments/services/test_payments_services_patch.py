import allure
import pytest

from source.api.payments.payments import create_service, delete_service, update_service_partially
from source.base.validator import (assert_status_code, assert_json_equal_json, assert_json_by_model)
from source.enums.expected import ExpectedJSON
from source.schemas.payments.external_payments_services_schema import External_Payments


@allure.epic('Payments')
@allure.feature('External Payments')
@allure.story('Services')
@allure.suite('Test patch services')
@pytest.mark.smoke
class TestPaymentsPostList:

    @allure.title('Check if we can not partially update service with an empty name')
    @allure.description(f"Проверка ответа [400] при частичном обновлении сервиса с пустым именем")
    def test_external_payments_services_id_negative_change_to_empty_value_patch(self):
        payload1 = {
            "name": "UNIQ"
        }

        response_1 = create_service(json=payload1)
        id_test = response_1.json().get("id")
        assert_status_code(response=response_1, expected=201)

        payload2 = {
            "name": ""
        }

        response_2 = update_service_partially(id_data=id_test, json=payload2)
        # expected = ExpectedJSON.FIELD_CANNOT_BE_EMPTY.value
        expected = {"name":["This field may not be blank."]}
        assert_status_code(response=response_2, expected=400)
        assert_json_equal_json(response=response_2, json=expected)

        response_3 = delete_service(id_data=id_test)
        assert_status_code(response=response_3, expected=204)

    @allure.title('Check if we can not partially update service with an empty name')
    @allure.description(f"Проверка ответа [400] при частичном обновлении сервиса с пустым именем (пробел)")
    def test_external_payments_services_id_negative_change_value_with_spaces_patch(self):
        payload1 = {
            "name": "UNIQ"
        }

        response_1 = create_service(json=payload1)
        id_test = response_1.json().get("id")
        assert_status_code(response=response_1, expected=201)

        payload2 = {
            "name": " "
        }

        response_2 = update_service_partially(id_data=id_test, json=payload2)
        expected = {"name": ["This field may not be blank."]}
        assert_status_code(response=response_2, expected=400)
        assert_json_equal_json(response=response_2, json=expected)

        response_3 = delete_service(id_data=id_test)
        assert_status_code(response=response_3, expected=204)

    @allure.title('Check of partially update service')
    @allure.description(f"Проверка ответа [200] при частичном обновлении сервиса")
    def test_external_payments_services_id_positive_patch(self):
        payload1 = {
            "name": "UNIQ"
        }

        response_1 = create_service(json=payload1)
        id_test = response_1.json().get("id")
        assert_status_code(response=response_1, expected=201)

        payload2 = {
            "name": "yookassa"
        }

        response_2 = update_service_partially(id_data=id_test, json=payload2)
        assert_status_code(response=response_2, expected=200)
        assert_json_by_model(response=response_2, model=External_Payments)

        response_3 = delete_service(id_data=id_test)
        assert_status_code(response=response_3, expected=204)
