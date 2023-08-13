import allure
import pytest

from source.api.games.filters import filters
from source.base.validator import assertions
from source.enums.data import Cases
from source.schemas.games.operating_system import OperatingSystem


@allure.epic('Games')
@allure.feature('Utils')
@allure.story('Filter by platform')
@allure.suite('Test get filters platforms list')
@pytest.mark.smoke
@pytest.mark.xfail(reason='The list items do not match the model')
class TestFiltersPlatforms:
    @allure.title(f'{Cases.GAMES["TG103"]["id"]}-Test filters platforms list')
    @allure.description('Проверка успешного ответа [200] при запросе фильтра по операционной системе')
    @allure.testcase(name=Cases.GAMES["TG103"]["name"], url=Cases.GAMES["TG103"]["link"])
    def test_filters_platforms_list(self):
        response = filters.platforms_list()
        assertions.status_code(actual=response.status_code, expected=200)
        assertions.json_by_model(actual=response.json(), model=OperatingSystem)
