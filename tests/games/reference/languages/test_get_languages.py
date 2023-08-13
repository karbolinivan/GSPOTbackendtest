from http import HTTPStatus

import allure
import pytest

from source.api.games.languages import languages
from source.enums.expected import ExpectedJSON
from source.enums.data import Cases
from source.schemas.games.laguage_schema import Language
from source.base.validator import assertions


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Languages')
@allure.suite('Test get languages')
@pytest.mark.smoke
class TestLanguages:
    @allure.title(f'{Cases.GAMES["TG93"]["id"]}-Test languages list')
    @allure.description('Проверка успешного ответа [200] при запросе списка языков.')
    @allure.testcase(name=Cases.GAMES["TG93"]["name"], url=Cases.GAMES["TG93"]["link"])
    def test_languages_list(self):
        response = languages.get_list()
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assertions.json_by_model(actual=response.json(), model=Language)

    @allure.title(f'{Cases.GAMES["TG97"]["id"]}-Test languages read')
    @allure.description('Проверка успешного ответа [200] при запросе языка по ID.')
    @allure.testcase(name=Cases.GAMES["TG97"]["name"], url=Cases.GAMES["TG97"]["link"])
    def test_languages_read(self, create_delete_test_languages):
        id_test = create_delete_test_languages.json().get('id')
        response = languages.get_id(id_data=id_test)
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assertions.json_by_model(actual=response.json(), model=Language)
        assertions.json_key_value(actual=response.json(), expected=create_delete_test_languages.json(), key='id')


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Languages')
@allure.suite('Regression-tests get languages')
@pytest.mark.regression
class TestLanguagesRegression:
    @allure.title(f'{Cases.GAMES["TG96"]["id"]}-Test read a language with a non-existent ID')
    @allure.description('Проверка ответа [404] при запросе языка c несуществующим ID')
    @allure.testcase(name=Cases.GAMES["TG96"]["name"], url=Cases.GAMES["TG96"]["link"])
    def test_language_read_with_non_existent_id(self):
        response = languages.get_id(id_data=-1)
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.NOT_FOUND)
        assertions.json_equal_json(actual=response.json(), expected=ExpectedJSON.NOT_FOUND.value)

    @allure.title(f'{Cases.GAMES["TG95"]["id"]}-Test read a language with a deleted ID')
    @allure.description('Проверка ответа [404] при запросе удаленного языка')
    @allure.testcase(name=Cases.GAMES["TG95"]["name"], url=Cases.GAMES["TG95"]["link"])
    def test_language_read_with_deleted_id(self, create_test_languages, delete_created_data):
        id_test = create_test_languages.json().get('id')
        delete_created_data(api=languages.delete, id_data=id_test)

        response = languages.get_id(id_data=id_test)
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.NOT_FOUND)
        assertions.json_equal_json(actual=response.json(), expected=ExpectedJSON.NOT_FOUND.value)
