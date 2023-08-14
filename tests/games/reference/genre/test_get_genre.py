from http import HTTPStatus

import allure
import pytest

from source.enums.data import Cases
from source.schemas.games.genre_schema import Genre
from source.api.games.genre import genres
from source.base.validator import assertions


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Genre')
@allure.suite('Test get genre')
@pytest.mark.smoke
class TestGenre:
    @allure.title(f'{Cases.GAMES["TG39"]["id"]}-Test genre list')
    @allure.description('Проверка успешного ответа [200] при запросе списка жанров')
    @allure.testcase(name=Cases.GAMES["TG39"]["name"], url=Cases.GAMES["TG39"]["link"])
    def test_genre_list(self):
        response = genres.get_list()
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assertions.json_by_model(actual=response.json(), model=Genre)

    @allure.title(f'{Cases.GAMES["TG49"]["id"]}-Test genre read')
    @allure.description('Проверка успешного ответа [200] при запросе жанра по ID.')
    @allure.testcase(name=Cases.GAMES["TG49"]["name"], url=Cases.GAMES["TG49"]["link"])
    def test_genre_read(self, create_delete_test_genre):
        id_test = create_delete_test_genre.json().get('id')
        response = genres.get_id(id_data=id_test)

        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assertions.json_by_model(actual=response.json(), model=Genre)
        assertions.json_key_value(actual=response.json(), expected=create_delete_test_genre.json(), key='id')
