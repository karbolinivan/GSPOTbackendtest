import allure
import pytest

from source.enums.data import Cases
from source.schemas.genre_games import GenreGames
from source.api.filters_genres import get_filters_genres_list
from source.base.validator import assert_status_code, assert_json_by_model


@allure.epic('Games')
@allure.feature('Utils')
@allure.story('Filter by genre')
@allure.suite('Test get filters genres list')
@pytest.mark.smoke
@pytest.mark.xfail(reason='The subgenre must contain required fields')
class TestFiltersGenres:
    @allure.title(f'{Cases.GAMES["TG102"]["id"]}-Test filters genres list')
    @allure.description('Проверка успешного ответа [200] при запросе фильтра по жанру игр')
    @allure.testcase(name=Cases.GAMES["TG102"]["name"], url=Cases.GAMES["TG102"]["link"])
    def test_filters_genres_list(self):
        response = get_filters_genres_list()
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=GenreGames)
