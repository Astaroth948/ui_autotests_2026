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
@pytest.mark.regression
@pytest.mark.registration
@allure.epic(AllureEpic.AUTHENTICATION)
@allure.parent_suite(AllureEpic.AUTHENTICATION)
@allure.feature(AllureFeature.FUNCTIONAL)
@allure.suite(AllureFeature.FUNCTIONAL)
@allure.story(AllureStory.REGISTRATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestFunctionalRegistration:
    @allure.severity(Severity.BLOCKER)
    @allure.title('Проверка регистрации с корректными данными')
    def test_successful_registration(self, auth_page: AuthPage, dashboard_page: DashboardPage):
        auth_page.visit(url=AppRoute.REGISTRATION)

        dashboard_page.check_visible_status_base_components(status=False, username=None)

        auth_page.registration_user(user_data=UsersData.DEFAULT_USER)

        dashboard_page.check_current_url(expected_url=AppRoute.DASHBOARD)
        dashboard_page.check_visible_status_base_components(status=True, username=UsersData.DEFAULT_USER.username)
