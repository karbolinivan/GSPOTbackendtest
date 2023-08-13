import allure
import pytest

from source.api.games.filters import filters
from source.base.validator import assertions
from source.enums.data import Cases
from source.schemas.games.genre_games import GenreGames


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
        response = filters.genres_list()
        assertions.status_code(actual=response.status_code, expected=200)
        assertions.json_by_model(actual=response.json(), model=GenreGames)
