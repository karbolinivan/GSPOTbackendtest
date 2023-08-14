from http import HTTPStatus

import allure
import pytest

from source.api.games.genre import genres
from source.base.generator import Generator
from source.schemas.games.genre_schema import Genre
from source.base.validator import assertions


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Genre')
@allure.suite('Test patch genre')
@pytest.mark.smoke
class TestGenrePartialUpdate:

    @allure.title('Test genre partial update')
    @allure.description('Проверка успешного ответа [200] при частичном обновлении жанра')
    def test_genre_partial_update(self, create_delete_test_genre):
        id_test = create_delete_test_genre.json().get('id')

        payload = Generator.object(model=Genre)
        response = genres.update_partly(id_data=id_test, json=payload)
        payload['id'] = id_test

        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assertions.json_by_model(actual=response.json(), model=Genre)
        assertions.json_equal_json(actual=response.json(), expected=payload)
        assertions.json_key_value(actual=response.json(), expected=payload, key='name')
