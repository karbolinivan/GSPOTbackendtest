from http import HTTPStatus

import allure
import pytest

from source.api.games.subgenre import subgenres
from source.base.generator import Generator
from source.base.validator import assertions
from source.schemas.games.subgenre import Subgenre


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Subgenre')
@allure.suite('Test put subgenre')
@pytest.mark.smoke
@pytest.mark.xfail(reason='Subgenre cannot be created')
class TestSubgenreUpdate:
    @allure.title('Test subgenre update')
    @allure.description('Проверка успешного ответа [201] при обновлении поджанра')
    def test_subgenre_update(self, create_delete_test_subgenre):
        id_test = create_delete_test_subgenre.json().get('id')

        payload = Generator.object(model=Subgenre)
        response = subgenres.update(id_data=id_test, json=payload)
        payload['id'] = id_test

        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assertions.json_by_model(actual=response.json(), model=Subgenre)
        assertions.json_equal_json(actual=response.json(), expected=payload)
        assertions.json_key_value(actual=response.json(), expected=payload, key='name')
