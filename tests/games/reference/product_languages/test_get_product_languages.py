from http import HTTPStatus

import allure
import pytest

from source.api.games.product_languages import product_languages
from source.base.validator import assertions
from source.enums.data import Cases
from source.schemas.games.product_languages import ProductLanguages


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Product languages')
@allure.suite('Test get product languages')
@pytest.mark.smoke
class TestProductLanguages:
    @allure.title(f'{Cases.GAMES["TG18"]["id"]} Test product languages list')
    @allure.description('Проверка успешного ответа [200] при запросе списка языков продукта')
    @allure.testcase(name=Cases.GAMES["TG18"]["name"], url=Cases.GAMES["TG18"]["link"])
    def test_product_languages_list(self):
        response = product_languages.get_list()
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assertions.json_by_model(actual=response.json(), model=ProductLanguages)

    @allure.title(f'{Cases.GAMES["TG20"]["id"]} Test product languages  read')
    @allure.description('Проверка успешного ответа [200] при запросе списка языков продукта')
    @pytest.mark.xfail(reason='Product languages cannot be created')
    @allure.testcase(name=Cases.GAMES["TG20"]["name"], url=Cases.GAMES["TG20"]["link"])
    def test_product_languages_read(self, create_delete_test_product_languages):
        id_test = create_delete_test_product_languages.json().get('id')
        response = product_languages.get_id(id_data=id_test)
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assertions.json_by_model(actual=response.json(), model=ProductLanguages)
