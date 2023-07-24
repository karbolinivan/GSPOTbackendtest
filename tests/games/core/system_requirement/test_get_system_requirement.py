import allure
import pytest

from source.api.games.system_requirement import get_system_requirement, get_system_requirement_list
from source.base.validator import assert_status_code, assert_json_by_model
from source.schemas.games.system_requirement import SystemRequirement


@allure.epic('Games')
@allure.feature('Core')
@allure.story('System requirement')
@allure.suite('Test get system requirement')
@pytest.mark.smoke
class TestSystemRequirement:
    @allure.title('Test system requirement')
    @allure.description('Проверка успешного ответа [200] при запросе списка системных требований.')
    def test_system_requirement_list(self):
        response = get_system_requirement_list()
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=SystemRequirement)

    @allure.title('Test system requirement read')
    @allure.description('Проверка успешного ответа [200] при запросе системных требований по ID.')
    def test_system_requirement_read(self):
        # id_test = create_delete_test_system_requirement.json().get('id')
        id_test = "6f98f5fe-8b36-4bc8-874e-0feeb910747a"
        response = get_system_requirement(id_data=id_test)
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=SystemRequirement)
