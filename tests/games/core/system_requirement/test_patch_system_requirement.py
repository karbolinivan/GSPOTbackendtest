from http import HTTPStatus

import allure
import pytest

from source.api.games.system_requirement import system_requirements
from source.base.generator import Generator
from source.base.validator import assertions
from source.enums.data import Cases
from source.schemas.games.system_requirement import SystemRequirement


@allure.epic('Games')
@allure.feature('Core')
@allure.story('System requirement')
@allure.suite('Test patch system requirement')
@pytest.mark.smoke
@pytest.mark.xfail(reason='System requirements cannot be created')
class TestSystemRequirementPartialUpdate:
    @allure.title(f'{Cases.GAMES["TG11"]["id"]} Test system requirement partial update')
    @allure.description('Проверка успешного ответа [200] при частичном обновлении системных требований')
    @allure.testcase(name=Cases.GAMES["TG11"]["name"], url=Cases.GAMES["TG11"]["link"])
    def test_system_requirement_partial_update(self, create_delete_test_system_requirement):
        id_test = create_delete_test_system_requirement.json().get('id')
        payload = Generator.object(model=SystemRequirement, include='deviceGraphics')

        response = system_requirements.update_partly(id_data=id_test, json=payload)
        payload['id'] = id_test

        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assertions.json_by_model(actual=response.json(), model=SystemRequirement)
        assertions.json_key_value(actual=response.json(), expected=payload, key='deviceGraphics')
