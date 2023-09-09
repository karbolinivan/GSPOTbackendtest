from http import HTTPStatus

import allure
import pytest

from source.api.games.system_requirement import system_requirements
from source.base.validator import assertions
from source.enums.data import Cases


@allure.epic('Games')
@allure.feature('Core')
@allure.story('System requirement')
@allure.suite('Test delete system requirement')
@pytest.mark.smoke
@pytest.mark.xfail(reason='System requirements cannot be created')
class TestSystemRequirementDelete:
    @allure.title(f'{Cases.GAMES["TG9"]["id"]} Test system requirement delete')
    @allure.description('Проверка успешного ответа [204] при удалении системных требований')
    @allure.testcase(name=Cases.GAMES["TG9"]["name"], url=Cases.GAMES["TG9"]["link"])
    def test_system_requirement_delete(self, create_test_system_requirement):
        id_test = create_test_system_requirement.json().get('id')
        response = system_requirements.delete(id_data=id_test)
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.NO_CONTENT)
