from http import HTTPStatus

import allure
import pytest

from source.api.games.system_requirement import system_requirements
from source.base.generator import Generator
from source.enums.data import Cases
from source.schemas.games.system_requirement import SystemRequirement
from source.base.validator import assertions


@allure.epic('Games')
@allure.feature('Core')
@allure.story('System requirement')
@allure.suite('Test put system requirement')
@pytest.mark.smoke
@pytest.mark.xfail(reason='System requirements cannot be created')
class TestSystemRequirementUpdate:
    @allure.title(f'{Cases.GAMES["TG14"]["id"]}-Test system requirement update')
    @allure.description('Проверка успешного ответа [201] при обновлении системных требований')
    @allure.testcase(name=Cases.GAMES["TG14"]["name"], url=Cases.GAMES["TG14"]["link"])
    def test_system_requirement_update(self, create_delete_test_system_requirement):
        id_test = create_delete_test_system_requirement.json().get('id')
        payload = Generator.object(model=SystemRequirement)

        response = system_requirements.update(id_data=id_test, json=payload)
        payload['id'] = id_test

        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assertions.json_by_model(actual=response.json(), model=SystemRequirement)
        assertions.json_equal_json(actual=response.json(), expected=payload)
