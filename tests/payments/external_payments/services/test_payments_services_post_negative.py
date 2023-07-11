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
    @allure.description('Проверка успешного ответа [400] при создании сервиса оплаты с некорректным именем {0}')
    @pytest.mark.parametrize("name, expected, message", [
        ("card", 400, ExpectedJSON.PAYMENT_SERVICE_WITH_THIS_NAME_ALREADY_EXIST.value),
        ("", 400, ExpectedJSON.FIELD_CANNOT_BE_EMPTY.value),
        ("fhjthgld3845unfjlcns30567fgcjk", 400, ExpectedJSON.PAYMENT_SERVICE_EXCEEDED_NAME_LENGTH.value),
        (" ", 400, ExpectedJSON.FIELD_CANNOT_BE_EMPTY.value),
        # empty body TODO
        # Создать дубликат поля "name" с разными значениями TODO
    ])
    def test_external_payments_services_negative_input_value_post(self, name, expected, message):
        response = create_service({"name": name})

        assert_status_code(response=response, expected=expected)
        assert_json_by_model(response=response, model=External_Payments)

        service_id = response.json()["id"]
        delete_service(service_id)
        
        print(response.text)
