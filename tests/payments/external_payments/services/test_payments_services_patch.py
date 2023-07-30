import allure
import pytest

from source.api.payments.payments import update_service_partially
from source.base.validator import (assert_status_code, assert_json_equal_json, assert_json_by_model)
from source.schemas.payments.external_payments.services_schema import Payments_Services


@allure.epic('Payments')
@allure.feature('External Payments')
@allure.story('Services')
@allure.suite('Test patch services')
@pytest.mark.smoke
class TestPaymentsPostList:

    @allure.title('Check if we can not partially update service with an empty name')
    @allure.description(f"Проверка ответа [400] при частичном обновлении сервиса с пустым именем")
    def test_external_payments_services_id_negative_change_to_empty_value_patch(self, create_delete_test_payment_service):

        id_test = create_delete_test_payment_service.json().get('id')

        payload = {
            "name": ""
        }

        response = update_service_partially(id_data=id_test, json=payload)
        expected = {"name":["This field may not be blank."]}
        assert_status_code(response=response, expected=400)
        assert_json_equal_json(response=response, json=expected)

    @allure.title('Check if we can not partially update service with an empty name')
    @allure.description(f"Проверка ответа [400] при частичном обновлении сервиса с пустым именем (пробел)")
    def test_external_payments_services_id_negative_change_value_with_spaces_patch(self, create_delete_test_payment_service):

        id_test = create_delete_test_payment_service.json().get('id')

        payload = {
            "name": " "
        }

        response = update_service_partially(id_data=id_test, json=payload)
        expected = {"name": ["This field may not be blank."]}
        assert_status_code(response=response, expected=400)
        assert_json_equal_json(response=response, json=expected)

    @allure.title('Check of partially update service')
    @allure.description(f"Проверка ответа [200] при частичном обновлении сервиса")
    def test_external_payments_services_id_positive_patch(self, create_delete_test_payment_service):

        id_test = create_delete_test_payment_service.json().get('id')

        payload = {
            "name": "yookassa"
        }

        response = update_service_partially(id_data=id_test, json=payload)
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Payments_Services)
