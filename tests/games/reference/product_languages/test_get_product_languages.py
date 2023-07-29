import allure
import pytest

from source.enums.data import Cases
from source.schemas.product_languages import ProductLanguages
from source.api.product_languages import get_product_languages_list, get_product_languages
from source.base.validator import assert_status_code, assert_json_key_value, assert_json_by_model


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Product languages')
@allure.suite('Test get product languages')
@pytest.mark.smoke
class TestProductLanguages:
    @allure.title(f'{Cases.GAMES["TG17"]["id"]}-Test product languages list')
    @allure.description('Проверка успешного ответа [200] при запросе списка языков продукта')
    @allure.testcase(name=Cases.GAMES["TG17"]["name"], url=Cases.GAMES["TG17"]["link"])
    def test_product_languages_list(self):
        response = get_product_languages_list()
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=ProductLanguages)

    @allure.title(f'{Cases.GAMES["TG19"]["id"]}-Test product languages  read')
    @allure.description('Проверка успешного ответа [200] при запросе списка языков продукта')
    @pytest.mark.xfail(reason='Product languages cannot be created')
    @allure.testcase(name=Cases.GAMES["TG19"]["name"], url=Cases.GAMES["TG19"]["link"])
    def test_product_languages_read(self, create_delete_test_product_languages):
        id_test = create_delete_test_product_languages.json().get('id')
        response = get_product_languages(id_data=id_test)
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=ProductLanguages)
        assert_json_key_value(response=response, json=response.json(), key='id')
