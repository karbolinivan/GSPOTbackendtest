from http import HTTPStatus

import allure
import pytest

from source.api.games.system_requirement import system_requirements
from source.base.validator import assertions
from source.enums.data import Cases
from source.schemas.games.system_requirement import SystemRequirement


@allure.epic('Games')
@allure.feature('Core')
@allure.story('System requirement')
@allure.suite('Test get system requirement')
@pytest.mark.smoke
class TestSystemRequirement:
    @allure.title(f'{Cases.GAMES["TG7"]["id"]} Test system requirement list')
    @allure.description('Проверка успешного ответа [200] при запросе списка системных требований.')
    @allure.testcase(name=Cases.GAMES["TG7"]["name"], url=Cases.GAMES["TG7"]["link"])
    def test_system_requirement_list(self):
        response = system_requirements.get_list()
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assertions.json_by_model(actual=response.json(), model=SystemRequirement)

    @allure.title(f'{Cases.GAMES["TG10"]["id"]} Test system requirement read')
    @allure.title('Test system requirement read')
    @allure.description('Проверка успешного ответа [200] при запросе системных требований по ID.')
    @allure.testcase(name=Cases.GAMES["TG10"]["name"], url=Cases.GAMES["TG10"]["link"])
    @pytest.mark.xfail(reason='System requirements cannot be created')
    def test_system_requirement_read(self, create_delete_test_system_requirement):
        id_test = create_delete_test_system_requirement.json().get('id')
        response = system_requirements.get_id(id_data=id_test)
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assertions.json_by_model(actual=response.json(), model=SystemRequirement)
