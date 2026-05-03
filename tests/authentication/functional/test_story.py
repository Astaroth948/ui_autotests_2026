import allure
import pytest
from allure_commons.types import Severity

from testdata.allure.epics import AllureEpic
from testdata.allure.features import AllureFeature
from testdata.allure.stories import AllureStory
from testdata.routes import AppRoute
from testdata.users import UsersData
from ui_course.pages.authentication.auth_page import AuthPage
from ui_course.pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.registration
@allure.epic(AllureEpic.AUTHENTICATION)
@allure.parent_suite(AllureEpic.AUTHENTICATION)
@allure.feature(AllureFeature.FUNCTIONAL)
@allure.suite(AllureFeature.FUNCTIONAL)
@allure.story(AllureStory.STORY)
@allure.sub_suite(AllureStory.STORY)
class TestFunctionalUserStoryAuth:
    @allure.severity(Severity.BLOCKER)
    @allure.title('Проверка регистрации и повторной авторизации')
    def test_registration_and_relogin(self, auth_page: AuthPage, dashboard_page: DashboardPage):
        auth_page.visit(url=AppRoute.REGISTRATION)
        auth_page.registration_user(user_data=UsersData.DEFAULT_USER)

        dashboard_page.check_current_url(expected_url=AppRoute.DASHBOARD)
        dashboard_page.sidebar.click_logout_button()

        auth_page.check_current_url(expected_url=AppRoute.LOGIN)
        dashboard_page.check_visible_status_base_components(status=False, username=None)

        auth_page.login_user(user_data=UsersData.DEFAULT_USER)
        dashboard_page.check_visible_status_base_components(status=True, username=UsersData.DEFAULT_USER.username)
