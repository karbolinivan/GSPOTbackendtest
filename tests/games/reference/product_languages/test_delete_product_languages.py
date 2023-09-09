from http import HTTPStatus

import allure
import pytest

from source.api.games.product_languages import product_languages
from source.base.validator import assertions
from source.enums.data import Cases


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Product languages')
@allure.suite('Test delete product languages')
@pytest.mark.smoke
@pytest.mark.xfail(reason='Product languages cannot be created')
class TestProductLanguagesDelete:
    @allure.title(f'{Cases.GAMES["TG17"]["id"]} Test product languages delete')
    @allure.description('Проверка успешного ответа [204] при удалении языка продукта')
    @allure.testcase(name=Cases.GAMES["TG17"]["name"], url=Cases.GAMES["TG17"]["link"])
    def test_product_languages_delete(self, create_test_product_languages):
        id_test = create_test_product_languages.json().get('id')
        response = product_languages.delete(id_data=id_test)
        assertions.status_code(actual=response.status_code, expected=HTTPStatus.NO_CONTENT)
