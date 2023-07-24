import allure
import pytest

from source.api.filters_platforms import get_filters_platforms_list
from source.base.validator import assert_status_code, assert_json_by_model
from source.schemas.operating_system import OperatingSystem


@allure.epic('Games')
@allure.feature('Utils')
@allure.story('Filter by platform')
@allure.suite('Test get filters platforms list')
@pytest.mark.smoke
@pytest.mark.xfail(reason='The list items do not match the model')
class TestFiltersPlatforms:
    @allure.title('Test filters platforms list')
    @allure.description('Проверка успешного ответа [200] при запросе фильтра по операционной системе')
    def test_filters_platforms_list(self):
        response = get_filters_platforms_list()
        assert_status_code(response=response, expected=200)
        assert_json_by_model(response=response, model=OperatingSystem)
