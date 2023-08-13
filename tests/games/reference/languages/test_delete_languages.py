from http import HTTPStatus

import allure
import pytest

from source.api.games.languages import languages
from source.base.validator import assertions
from source.enums.data import Cases
from source.enums.expected import ExpectedJSON


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Languages')
@allure.suite('Test delete languages')
@pytest.mark.smoke
class TestLanguagesDelete:
    @allure.title(f'{Cases.GAMES["TG92"]["id"]}-Test languages delete')
    @allure.description('Проверка успешного ответа [204] при удалении языка')
    @allure.testcase(name=Cases.GAMES["TG92"]["name"], url=Cases.GAMES["TG92"]["link"])
    def test_languages_delete(self, create_test_languages):
        id_test = create_test_languages.json().get('id')
        response = languages.delete(id_data=id_test)
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.NO_CONTENT)


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Languages')
@allure.suite('Regression-tests delete languages')
@pytest.mark.regression
class TestLanguagesDeleteRegression:
    @allure.title(f'{Cases.GAMES["TG91"]["id"]}-Test deleting a language with a non-existent ID')
    @allure.description('Проверка ответа [404] при удалении языка c несуществующим ID')
    @allure.testcase(name=Cases.GAMES["TG91"]["name"], url=Cases.GAMES["TG91"]["link"])
    def test_language_delete_with_non_existent_id(self):
        response = languages.delete(id_data=-1)
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.NOT_FOUND)
        assertions.json_equal_json(actual=response.json(), expected=ExpectedJSON.NOT_FOUND.value)
