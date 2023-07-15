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
    def test_external_payments_services_positive_input_value_post(self, name, expected, message):
        response = create_service({"name": name})

        assert_status_code(response=response, expected=expected)
        assert_json_by_model(response=response, model=External_Payments)
        print(response.json())

        service_id = response.json().get("id")
        if service_id:
            delete_response = delete_service(service_id)
            assert delete_response.status_code == 200, "Unable to delete"

        print(response.text)