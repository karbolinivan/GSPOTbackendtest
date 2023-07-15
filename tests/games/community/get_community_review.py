import allure
import pytest

from source.api.games.community import get_community_review
from source.base.validator import assert_status_code


@allure.epic('Games')
@allure.feature('Community')
@allure.story('Review')
@allure.suite('Test get community review')
@pytest.mark.smoke
class TestCommunityReview:
    @allure.title('Test community review read')
    @allure.description('Проверка успешного ответа [200] при запросе обзора пользователей.')
    def test_community_review_read(self):
        id_test = '6f98f5fe-8b36-4bc8-874e-0feeb910747a'
        response = get_community_review(id_data=id_test)
        assert_status_code(response=response, expected=200)
