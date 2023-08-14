from http import HTTPStatus

import allure
import pytest

from source.api.games.subgenre import subgenres
from source.base.validator import assertions


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Subgenre')
@allure.suite('Test delete subgenre')
@pytest.mark.smoke
@pytest.mark.xfail(reason='Subgenre cannot be created')
class TestSubgenreDelete:
    @allure.title('Test subgenre delete')
    @allure.description('Проверка успешного ответа [204] при удалении поджанра')
    def test_subgenre_delete(self, create_test_subgenre):
        id_test = create_test_subgenre.json().get('id')
        response = subgenres.delete(id_data=id_test)
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.NO_CONTENT)
