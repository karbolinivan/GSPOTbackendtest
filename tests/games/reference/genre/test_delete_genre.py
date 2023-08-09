import allure
import pytest

from source.api.genre import delete_genre
from source.base.validator import assert_status_code
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
        response = delete_genre(id_data=id_test)
        assert_status_code(response=response, expected=204)
