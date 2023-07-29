import allure
import pytest

from source.api.games.system_requirement import delete_system_requirement
from source.base.validator import assert_status_code
from source.enums.data import Cases


@allure.epic('Games')
@allure.feature('Core')
@allure.story('System requirement')
@allure.suite('Test delete system requirement')
@pytest.mark.smoke
@pytest.mark.xfail(reason='System requirements cannot be created')
class TestSystemRequirementDelete:
    @allure.title(f'{Cases.GAMES["TG11"]["id"]}-Test system requirement delete')
    @allure.description('Проверка успешного ответа [204] при удалении системных требований')
    @allure.testcase(name=Cases.GAMES["TG11"]["name"], url=Cases.GAMES["TG11"]["link"])
    def test_system_requirement_delete(self, create_test_system_requirement):
        id_test = create_test_system_requirement.json().get('id')
        response = delete_system_requirement(id_data=id_test)
        assert_status_code(response=response, expected=204)
