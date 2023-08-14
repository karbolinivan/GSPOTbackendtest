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
@allure.suite('Test post system requirement')
@pytest.mark.smoke
@pytest.mark.xfail(reason='System requirements cannot be created')
class TestSystemRequirementCreate:
    @allure.title(f'{Cases.GAMES["TG10"]["id"]}-Test system requirement create')
    @allure.description('Проверка успешного ответа [201] при создании системных требований')
    @allure.testcase(name=Cases.GAMES["TG10"]["name"], url=Cases.GAMES["TG10"]["link"])
    def test_system_requirement_create(self):
        payload = Generator.object(model=SystemRequirement, seed=10)
        response = system_requirements.create(json=payload)

        payload['id'] = response.json().get('id')

        assertions.status_code(actual=response.status_code, expected=HTTPStatus.CREATED)
        assertions.json_by_model(actual=response.json(), model=SystemRequirement)
        assertions.json_equal_json(actual=response.json(), expected=payload)

        id_data = response.json().get('id')
        system_requirements.delete(id_data=id_data)
