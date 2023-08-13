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
@allure.suite('Test post Subgenre')
@pytest.mark.smoke
@pytest.mark.xfail(reason='Subgenre cannot be created')
class TestGenreCreate:
    @allure.title('Test subgenre create')
    @allure.description('Проверка успешного ответа [201] при создании поджанра')
    def test_subgenre_create(self, delete_created_data):
        payload = Generator.object(model=Subgenre)
        response = subgenres.create(json=payload)

        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assertions.json_by_model(actual=response.json(), model=Subgenre)
        assertions.json_key_value(actual=response.json(), expected=payload, key='name')

        id_data = response.json().get('id')
        delete_created_data(api=subgenres.delete, id_data=id_data)
