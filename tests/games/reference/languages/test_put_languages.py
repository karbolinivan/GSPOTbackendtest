import json
from http import HTTPStatus

import allure
import pytest

from source.api.games.languages import languages
from source.base.generator import Generator
from source.base.validator import assertions
from source.enums.data import Cases
from source.enums.expected import ExpectedJSON
from source.schemas.games.laguage_schema import Language


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
        response = languages.update(id_data=id_test, json=payload)
        payload['id'] = id_test

        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assertions.json_by_model(actual=response.json(), model=Language)
        assertions.json_equal_json(actual=response.json(), expected=payload)
        assertions.json_key_value(actual=response.json(), expected=payload, key='name')


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Languages')
@allure.suite('Regression-test put languages')
@pytest.mark.regression
class TestLanguagesUpdateRegression:
    @allure.title('{id_test_case}-Test languages update with invalid value')
    @allure.description('Проверка ответа [400] при обновлении языка с невалидным значением ')
    @pytest.mark.parametrize("id_test_case, name, link, value", [
        Cases.get_parametrize(service="Games", test_case="TG98"),
        Cases.get_parametrize(service="Games", test_case="TG99")
    ])
    def test_languages_update_with_invalid_name(self, id_test_case, name, link, value, create_delete_test_languages):
        allure.dynamic.testcase(name=name, url=link)

        id_test = create_delete_test_languages.json().get('id')
        response = languages.update(id_data=id_test, json=json.loads(value))

        expected = ExpectedJSON.key_value(key='name', value=ExpectedJSON.FIELD_CANNOT_BE_EMPTY_RUS.value)
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.BAD_REQUEST)
        assertions.json_equal_json(actual=response.json(), expected=expected)
