import json
import allure
import pytest

from source.base.generator import Generator
from source.enums.data import Cases
from source.enums.expected import ExpectedJSON
from source.schemas.laguage_schema import Language
from source.api.languages import create_languages, delete_languages
from source.base.validator import (assert_json_by_model, assert_json_key_value,
                                   assert_status_code, assert_json_equal_json)


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
        response = create_languages(json=payload)

        assert_status_code(response=response, expected=201)
        assert_json_by_model(response=response, model=Language)
        assert_json_key_value(response=response, json=payload, key='name')

        id_data = response.json().get("id")
        delete_created_data(api=delete_languages, id_data=id_data)


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Languages')
@allure.suite('Regression-tests post languages')
@pytest.mark.regression
class TestLanguagesCreateRegression:
    @allure.title('{id_test}-Test languages create with checking the boundary values')
    @allure.description('Проверка граничных значений поля "name" при создании языка')
    @pytest.mark.parametrize("id_test, name, link, value", [
        Cases.get_parametrize(test_case="TG76"),
        Cases.get_parametrize(test_case="TG77"),
        Cases.get_parametrize(test_case="TG87"),
        Cases.get_parametrize(test_case="TG89")
    ])
    def test_languages_create_with_boundary_values(self, id_test, name, link, value, delete_created_data):
        allure.dynamic.testcase(name=name, url=link)
        payload = json.loads(value)
        response = create_languages(json=payload)
        if len(payload["name"]) < 1:
            expected_json = ExpectedJSON.key_value(key='name', value=ExpectedJSON.FIELD_CANNOT_BE_EMPTY_RUS.value)
            assert_status_code(response=response, expected=400)
            assert_json_equal_json(response=response, json=expected_json)
        elif len(payload["name"]) > 100:
            expected_json = ExpectedJSON.key_value(key='name', value=ExpectedJSON.FIELD_CANNOT_CONTAINS_MORE_100.value)
            assert_status_code(response=response, expected=400)
            assert_json_equal_json(response=response, json=expected_json)
        else:
            assert_status_code(response=response, expected=201)
            assert_json_by_model(response=response, model=Language)
            assert_json_key_value(response=response, json=payload, key='name')

            id_data = response.json().get("id")
            delete_created_data(api=delete_languages, id_data=id_data)

    @allure.title('{id_test}-Test languages create with invalid name')
    @allure.description('Проверка ответа [400] при создании языка c невалидным значением')
    @pytest.mark.parametrize("id_test, name, link, value", [
        Cases.get_parametrize(test_case="TG81"),
        Cases.get_parametrize(test_case="TG82"),
        Cases.get_parametrize(test_case="TG83"),
        Cases.get_parametrize(test_case="TG84"),
        Cases.get_parametrize(test_case="TG85"),
        Cases.get_parametrize(test_case="TG88")
    ])
    @pytest.mark.xfail(reason='Should the answer be 400?')
    def test_languages_create_with_invalid_name(self, id_test, name, link, value, delete_created_data):
        allure.dynamic.testcase(name=name, url=link)
        payload = json.loads(value)
        response = create_languages(json=payload)

        if response.status_code == 201:
            id_data = response.json().get("id")
            delete_created_data(api=delete_languages, id_data=id_data)

        expected = ExpectedJSON.key_value(key='name', value=ExpectedJSON.FIELD_CANNOT_BE_EMPTY_RUS.value)
        assert_status_code(response=response, expected=400)
        assert_json_equal_json(response=response, json=expected)

    @allure.title('{id_test}-Test languages create with atypical value')
    @allure.description('Проверка ответа [200] при создании нетипичного значения языка')
    @pytest.mark.parametrize("id_test, name, link, value", [
        Cases.get_parametrize(test_case="TG78"),
        Cases.get_parametrize(test_case="TG79"),
        Cases.get_parametrize(test_case="TG86")
    ])
    def test_languages_create_with_atypical_value(self, id_test, name, link, value, delete_created_data):
        allure.dynamic.testcase(name=name, url=link)
        payload = json.loads(value)
        response = create_languages(json=payload)

        payload['name'] = payload['name'].strip()
        assert_status_code(response=response, expected=201)
        assert_json_by_model(response=response, model=Language)
        assert_json_key_value(response=response, json=payload, key='name')

        id_data = response.json().get("id")
        delete_created_data(api=delete_languages, id_data=id_data)
