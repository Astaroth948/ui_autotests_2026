import allure
import pytest
from allure_commons.types import Severity

from testdata.allure.epics import AllureEpic
from testdata.allure.features import AllureFeature
from testdata.allure.stories import AllureStory
from testdata.routes import AppRoute
from testdata.text import AlertsText
from testdata.users import UsersData
from ui_course.pages.authentication.auth_page import AuthPage
from ui_course.pages.authentication.models import IncorrectUserModel


@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.authorization
@allure.epic(AllureEpic.AUTHENTICATION)
@allure.parent_suite(AllureEpic.AUTHENTICATION)
@allure.feature(AllureFeature.FUNCTIONAL)
@allure.suite(AllureFeature.FUNCTIONAL)
@allure.story(AllureStory.LOGIN)
@allure.sub_suite(AllureStory.LOGIN)
class TestFunctionalLogin:
    @allure.severity(Severity.CRITICAL)
    @allure.title(f'Проверка алерта некорректной авторизации "{AlertsText.WRONG_EMAIL_OR_PASSWORD}"')
    @pytest.mark.parametrize(
        'incorrect_user_data',
        [pytest.param({'email': '  '}), pytest.param({'password': '  '}), pytest.param({'password': '1234567'})],
    )
    def test_wrong_email_or_password_alert_login(self, auth_page: AuthPage, incorrect_user_data: dict):
        auth_page.visit(url=AppRoute.LOGIN)

        auth_page.header.check_visible_status_header(status=True)
        auth_page.toolbar.check_login_mode()
        auth_page.alerts.check_visible_status_wrong_email_or_password_alert(status=False)

        user_data_dict = UsersData.DEFAULT_USER.model_dump()
        user_data_dict.update(incorrect_user_data)
        user_data = IncorrectUserModel(**user_data_dict)

        auth_page.login_form.fill(user_data=user_data)
        auth_page.toolbar.click_login_button()
        auth_page.alerts.check_visible_status_wrong_email_or_password_alert(status=True)
        auth_page.check_current_url(expected_url=AppRoute.LOGIN)
        auth_page.header.check_visible_status_header(status=True)
