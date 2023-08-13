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
@allure.suite('Test post languages')
@pytest.mark.smoke
class TestLanguagesCreate:
    @allure.title(f'{Cases.GAMES["TG90"]["id"]}-Test languages create')
    @allure.description('Проверка успешного ответа [201] при создании языка.')
    @allure.testcase(name=Cases.GAMES["TG90"]["name"], url=Cases.GAMES["TG90"]["link"])
    def test_languages_create(self, delete_created_data):
        payload = Generator.object(model=Language, seed=1)
        response = languages.create(json=payload)

        assertions.status_code(actual=response.status_code, expected=HTTPStatus.CREATED)
        assertions.json_by_model(actual=response.json(), model=Language)
        assertions.json_key_value(actual=response.json(), expected=payload, key='name')

        id_data = response.json().get("id")
        delete_created_data(api=languages.delete, id_data=id_data)


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Languages')
@allure.suite('Regression-tests post languages')
@pytest.mark.regression
class TestLanguagesCreateRegression:
    @allure.title('{id_test_case}-Test languages create with checking the boundary values')
    @allure.description('Проверка граничных значений поля "name" при создании языка')
    @pytest.mark.parametrize("id_test_case, name, link, value", [
        Cases.get_parametrize(service="Games", test_case="TG76"),
        Cases.get_parametrize(service="Games", test_case="TG77"),
        Cases.get_parametrize(service="Games", test_case="TG87"),
        Cases.get_parametrize(service="Games", test_case="TG89")
    ])
    def test_languages_create_with_boundary_values(self, id_test_case, name, link, value, delete_created_data):
        allure.dynamic.testcase(name=name, url=link)
        payload = json.loads(value)
        response = languages.create(json=payload)
        if len(payload["name"]) < 1:
            expected_json = ExpectedJSON.key_value(key='name', value=ExpectedJSON.FIELD_CANNOT_BE_EMPTY_RUS.value)
            assertions.status_code(actual=response.status_code, expected=HTTPStatus.BAD_REQUEST)
            assertions.json_equal_json(actual=response.json(), expected=expected_json)
        elif len(payload["name"]) > 100:
            expected_json = ExpectedJSON.key_value(key='name', value=ExpectedJSON.FIELD_CANNOT_CONTAINS_MORE_100.value)
            assertions.status_code(actual=response.status_code, expected=HTTPStatus.BAD_REQUEST)
            assertions.json_equal_json(actual=response.json(), expected=expected_json)
        else:
            assertions.status_code(actual=response.status_code, expected=201)
            assertions.json_by_model(actual=response.json(), model=Language)
            assertions.json_key_value(actual=response.json(), expected=payload, key='name')

            id_data = response.json().get("id")
            delete_created_data(api=languages.delete, id_data=id_data)

    @allure.title('{id_test_case}-Test languages create with invalid name')
    @allure.description('Проверка ответа [400] при создании языка c невалидным значением')
    @pytest.mark.parametrize("id_test_case, name, link, value", [
        Cases.get_parametrize(service="Games", test_case="TG81"),
        Cases.get_parametrize(service="Games", test_case="TG82"),
        Cases.get_parametrize(service="Games", test_case="TG83"),
        Cases.get_parametrize(service="Games", test_case="TG84"),
        Cases.get_parametrize(service="Games", test_case="TG85"),
        Cases.get_parametrize(service="Games", test_case="TG88")
    ])
    @pytest.mark.xfail(reason='Should the answer be 400?')
    def test_languages_create_with_invalid_name(self, id_test_case, name, link, value, delete_created_data):
        allure.dynamic.testcase(name=name, url=link)
        payload = json.loads(value)
        response = languages.create(json=payload)

        if response.status_code == 201:
            id_data = response.json().get("id")
            delete_created_data(api=languages.delete, id_data=id_data)

        expected = ExpectedJSON.key_value(key='name', value=ExpectedJSON.FIELD_CANNOT_BE_EMPTY_RUS.value)
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.BAD_REQUEST)
        assertions.json_equal_json(actual=response.json(), expected=expected)

    @allure.title('{id_test_case}-Test languages create with atypical value')
    @allure.description('Проверка ответа [200] при создании нетипичного значения языка')
    @pytest.mark.parametrize("id_test_case, name, link, value", [
        Cases.get_parametrize(service="Games", test_case="TG78"),
        Cases.get_parametrize(service="Games", test_case="TG79"),
        Cases.get_parametrize(service="Games", test_case="TG86")
    ])
    def test_languages_create_with_atypical_value(self, id_test_case, name, link, value, delete_created_data):
        allure.dynamic.testcase(name=name, url=link)
        payload = json.loads(value)
        response = languages.create(json=payload)

        payload['name'] = payload['name'].strip()
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.CREATED)
        assertions.json_by_model(actual=response.json(), model=Language)
        assertions.json_key_value(actual=response.json(), expected=payload, key='name')

        id_data = response.json().get("id")
        delete_created_data(api=languages.delete, id_data=id_data)
