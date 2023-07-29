import allure
import pytest

from source.api.games.system_requirement import get_system_requirement, get_system_requirement_list
from source.base.validator import assert_status_code, assert_json_by_model
from source.enums.data import Cases
from source.schemas.games.system_requirement import SystemRequirement


@allure.epic('Games')
@allure.feature('Core')
@allure.story('System requirement')
@allure.suite('Test get system requirement')
@pytest.mark.smoke
class TestSystemRequirement:
    @allure.title(f'{Cases.GAMES["TG9"]["id"]}-Test system requirement list')
    @allure.description('Проверка успешного ответа [200] при запросе списка системных требований.')
    @allure.testcase(name=Cases.GAMES["TG9"]["name"], url=Cases.GAMES["TG9"]["link"])
    def test_system_requirement_list(self):
        response = get_system_requirement_list()
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=SystemRequirement)

    @allure.title(f'{Cases.GAMES["TG12"]["id"]}-Test system requirement list')
    @allure.title('Test system requirement read')
    @allure.description('Проверка успешного ответа [200] при запросе системных требований по ID.')
    @allure.testcase(name=Cases.GAMES["TG12"]["name"], url=Cases.GAMES["TG12"]["link"])
    @pytest.mark.xfail(reason='System requirements cannot be created')
    def test_system_requirement_read(self, create_delete_test_system_requirement):
        id_test = create_delete_test_system_requirement.json().get('id')
        response = get_system_requirement(id_data=id_test)
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=SystemRequirement)
