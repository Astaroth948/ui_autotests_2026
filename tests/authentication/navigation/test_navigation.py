import allure
import pytest
from allure_commons.types import Severity

from testdata.allure.epics import AllureEpic
from testdata.allure.features import AllureFeature
from testdata.allure.stories import AllureStory
from testdata.routes import AppRoute
from ui_course.pages.authentication.auth_page import AuthPage


@pytest.mark.navigation
@pytest.mark.regression
@pytest.mark.authorization
@allure.epic(AllureEpic.AUTHENTICATION)
@allure.parent_suite(AllureEpic.AUTHENTICATION)
@allure.feature(AllureFeature.NAVIGATION)
@allure.suite(AllureFeature.NAVIGATION)
@allure.story(AllureStory.LINKED_PAGES)
@allure.sub_suite(AllureStory.LINKED_PAGES)
class TestNavigationAuth:
    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка перехода со страницы логина на страницу регистрации')
    def test_navigation_from_login_to_registration_page(self, auth_page: AuthPage):
        auth_page.visit(url=AppRoute.LOGIN)

        auth_page.check_current_url(expected_url=AppRoute.LOGIN)
        auth_page.header.check_visible_status_header(status=True)
        auth_page.toolbar.check_login_mode()
        auth_page.toolbar.click_registration_link()

        auth_page.check_current_url(expected_url=AppRoute.REGISTRATION)
        auth_page.header.check_visible_status_header(status=True)
        auth_page.toolbar.check_registration_mode()

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка перехода со страницы регистрации на страницу логина')
    def test_navigation_from_registration_to_login_page(self, auth_page: AuthPage):
        auth_page.visit(url=AppRoute.REGISTRATION)

        auth_page.check_current_url(expected_url=AppRoute.REGISTRATION)
        auth_page.header.check_visible_status_header(status=True)
        auth_page.toolbar.check_registration_mode()
        auth_page.toolbar.click_login_link()

        auth_page.check_current_url(expected_url=AppRoute.LOGIN)
        auth_page.header.check_visible_status_header(status=True)
        auth_page.toolbar.check_login_mode()
