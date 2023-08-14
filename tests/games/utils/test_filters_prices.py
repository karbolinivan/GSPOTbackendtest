import allure
import pytest

from source.api.games.filters import filters
from source.base.validator import assertions
from source.enums.data import Cases
from source.schemas.games.min_max_price import MinMaxPrice


@allure.epic('Games')
@allure.feature('Utils')
@allure.story('Filter by price')
@allure.suite('Test get filters prices list')
@pytest.mark.smoke
class TestFiltersPrices:
    @allure.title(f'{Cases.GAMES["TG104"]["id"]}-Test filters prices list')
    @allure.description('Проверка успешного ответа [200] при запросе списка фльтра цены')
    @allure.testcase(name=Cases.GAMES["TG104"]["name"], url=Cases.GAMES["TG104"]["link"])
    def test_filters_prices_list(self):
        response = filters.prices_list()
        assertions.status_code(actual=response.status_code, expected=200)
        assertions.json_by_model(actual=response.json(), model=MinMaxPrice)
