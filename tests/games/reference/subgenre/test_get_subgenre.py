from http import HTTPStatus

import allure
import pytest

from source.api.games.subgenre import subgenres
from source.base.validator import assertions
from source.enums.data import Cases
from source.schemas.games.subgenre import Subgenre


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Subgenre')
@allure.suite('Test get subgenre')
@pytest.mark.smoke
class TestSubgenre:
    @allure.title(f'{Cases.GAMES["TG102"]["id"]} Test subgenre list')
    @allure.description('Проверка успешного ответа [200] при запросе списка поджанров')
    @allure.testcase(name=Cases.GAMES["TG102"]["name"], url=Cases.GAMES["TG102"]["link"])
    def test_subgenre_list(self):
        response = subgenres.get_list()
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assertions.json_by_model(actual=response.json(), model=Subgenre)

    @allure.title('Test subgenre read')
    @allure.description('Проверка успешного ответа [200] при запросе поджанра по ID.')
    @pytest.mark.xfail(reason='Subgenre cannot be created')
    def test_genre_read(self, create_delete_test_subgenre):
        id_test = create_delete_test_subgenre.json().get('id')
        response = subgenres.get_id(id_data=id_test)
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assertions.json_by_model(actual=response.json(), model=Subgenre)
        assertions.json_key_value(actual=response.json(), expected=create_delete_test_subgenre.json(), key='name')
