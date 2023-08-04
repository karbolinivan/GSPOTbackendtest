import allure
import pytest

from source.api.product_languages import delete_product_languages
from source.base.validator import assert_status_code
from source.enums.data import Cases


@allure.epic('Games')
@allure.feature('Reference')
@allure.story('Product languages')
@allure.suite('Test delete product languages')
@pytest.mark.smoke
@pytest.mark.xfail(reason='Product languages cannot be created')
class TestProductLanguagesDelete:
    @allure.title(f'{Cases.GAMES["TG16"]["id"]}-Test product languages delete')
    @allure.description('Проверка успешного ответа [204] при удалении языка продукта')
    @allure.testcase(name=Cases.GAMES["TG16"]["name"], url=Cases.GAMES["TG16"]["link"])
    def test_product_languages_delete(self, create_test_product_languages):
        id_test = create_test_product_languages.json().get('id')
        response = delete_product_languages(id_data=id_test)
        assert_status_code(response=response, expected=204)
