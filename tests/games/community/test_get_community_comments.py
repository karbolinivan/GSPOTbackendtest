import allure
import pytest

from source.api.games.community import get_community_comments
from source.base.validator import assert_status_code
from source.enums.data import Cases


@allure.epic('Games')
@allure.feature('Community')
@allure.story('Comments')
@allure.suite('Test get community comments')
@pytest.mark.smoke
class TestCommunityComments:
    @allure.title(f'{Cases.GAMES["TG1"]["id"]}-Test community comments read')
    @allure.description('Проверка успешного ответа [200] при запросе коментариев пользователей.')
    @allure.testcase(name=Cases.GAMES["TG1"]["name"], url=Cases.GAMES["TG1"]['link'])
    def test_community_comments_read(self):
        id_test = 1
        response = get_community_comments(id_data=id_test)
        assert_status_code(response=response, expected=200)
