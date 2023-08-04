import allure
import pytest

from source.api.languages import delete_languages
from source.base.validator import assert_status_code, assert_json_equal_json
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
        response = delete_languages(id_data=id_test)
        assert_status_code(response=response, expected=204)


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
        response = delete_languages(id_data=-1)
        assert_status_code(response=response, expected=404)
        assert_json_equal_json(response=response, json=ExpectedJSON.NOT_FOUND.value)
