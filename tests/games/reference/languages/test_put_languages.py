import json
import allure
import pytest

from source.base.generator import Generator
from source.api.languages import update_languages
from source.enums.expected import ExpectedJSON
from source.enums.data import Cases
from source.schemas.laguage_schema import Language
from source.base.validator import (assert_json_by_model, assert_status_code,
                                   assert_json_key_value, assert_json_equal_json)


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Languages')
@allure.suite('Test put languages')
@pytest.mark.smoke
class TestLanguagesUpdate:
    @allure.title(f'{Cases.GAMES["TG100"]["id"]}-Test languages update')
    @allure.description('Проверка успешного ответа [200] при обновлении языка')
    @allure.testcase(name=Cases.GAMES["TG100"]["name"], url=Cases.GAMES["TG100"]["link"])
    def test_languages_update(self, create_delete_test_languages):
        id_test = create_delete_test_languages.json().get('id')

        payload = Generator.object(model=Language, seed=2)
        response = update_languages(id_data=id_test, json=payload)
        payload['id'] = id_test

        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=Language)
        assert_json_equal_json(response=response, json=payload)
        assert_json_key_value(response=response, json=payload, key='name')


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Languages')
@allure.suite('Regression-test put languages')
@pytest.mark.regression
class TestLanguagesUpdateRegression:
    @allure.title('{id_test_case}-Test languages update with invalid value')
    @allure.description('Проверка ответа [400] при обновлении языка с невалидным значением ')
    @pytest.mark.parametrize("id_test_case, name, link, value", [
        Cases.get_parametrize(test_case="TG98"), Cases.get_parametrize(test_case="TG99")
    ])
    def test_languages_update_with_invalid_name(self, id_test_case, name, link, value, create_delete_test_languages):
        allure.dynamic.testcase(name=name, url=link)
        id_test = create_delete_test_languages.json().get('id')

        response = update_languages(id_data=id_test, json=json.loads(value))

        expected = ExpectedJSON.key_value(key='name', value=ExpectedJSON.FIELD_CANNOT_BE_EMPTY_RUS.value)
        assert_status_code(response=response, expected=400)
        assert_json_equal_json(response=response, json=expected)
