from http import HTTPStatus

import allure
import pytest

from source.api.games.genre import genres
from source.base.validator import assertions
from source.enums.data import Cases


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Genre')
@allure.suite('Test delete genre')
@pytest.mark.smoke
class TestGenreDelete:
    @allure.title(f'{Cases.GAMES["TG26"]["id"]}-Test genre delete')
    @allure.description('Проверка успешного ответа [204] при удалении жанра')
    @allure.testcase(name=Cases.GAMES["TG26"]["name"], url=Cases.GAMES["TG26"]["link"])
    def test_genre_delete(self, create_test_genre):
        id_test = create_test_genre.json().get('id')
        response = genres.delete(id_data=id_test)
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.NO_CONTENT)
