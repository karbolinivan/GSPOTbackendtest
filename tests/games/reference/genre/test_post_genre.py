from http import HTTPStatus

import allure
import pytest

from source.base.generator import Generator
from source.enums.data import Cases
from source.schemas.games.genre_schema import Genre
from source.api.games.genre import genres
from source.base.validator import assertions


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Genre')
@allure.suite('Test post genre')
@pytest.mark.smoke
class TestGenreCreate:

    @allure.title(f'{Cases.GAMES["TG75"]["id"]} Test genre create')
    @allure.description('Проверка успешного ответа [201] при создании жанра')
    @allure.testcase(name=Cases.GAMES["TG75"]["name"], url=Cases.GAMES["TG75"]["link"])
    def test_genre_create(self, delete_created_data):
        payload = Generator.object(model=Genre)
        response = genres.create(json=payload)

        assertions.status_code(actual=response.status_code, expected=HTTPStatus.CREATED)
        assertions.json_by_model(actual=response.json(), model=Genre)
        assertions.json_key_value(actual=response.json(), expected=payload, key='name')

        id_data = response.json().get('id')
        delete_created_data(api=genres.delete, id_data=id_data)
