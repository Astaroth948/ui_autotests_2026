import allure
import pytest
from allure_commons.types import Severity

from testdata.allure.epics import AllureEpic
from testdata.allure.features import AllureFeature
from testdata.allure.stories import AllureStory
from testdata.routes import AppRoute
from testdata.users import UsersData
from ui_course.pages.authentication.auth_page import AuthPage
from ui_course.pages.authentication.models import IncorrectUserModel


@pytest.mark.view
@pytest.mark.regression
@pytest.mark.authorization
@allure.epic(AllureEpic.AUTHENTICATION)
@allure.parent_suite(AllureEpic.AUTHENTICATION)
@allure.feature(AllureFeature.VIEW)
@allure.suite(AllureFeature.VIEW)
@allure.story(AllureStory.LOGIN)
@allure.sub_suite(AllureStory.LOGIN)
class TestViewAuthorization:
    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка дефолтного состояния страницы авторизации')
    def test_default_state_login_page(self, auth_page: AuthPage):
        auth_page.visit(url=AppRoute.LOGIN)

        auth_page.header.check_visible_status_header(status=True)
        auth_page.toolbar.check_login_mode()
        auth_page.login_form.check_filling(user_data=UsersData.EMPTY_FORM)
        auth_page.toolbar.check_enable_status_login_button(status=False)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка состояния активности кнопки "Login" при заполнении некорректных данных пользователя')
    @pytest.mark.parametrize('incorrect_user_data', [pytest.param({'email': ''}), pytest.param({'password': ''})])
    def test_status_login_button_when_filling_incorrect_user_data(self, auth_page: AuthPage, incorrect_user_data: dict):
        auth_page.visit(url=AppRoute.LOGIN)

        auth_page.login_form.fill(user_data=UsersData.DEFAULT_USER)
        auth_page.toolbar.check_enable_status_login_button(status=True)

        user_data_dict = UsersData.DEFAULT_USER.model_dump()
        user_data_dict.update(incorrect_user_data)
        user_data = IncorrectUserModel(**user_data_dict)

        auth_page.login_form.fill(user_data=user_data)
        auth_page.toolbar.check_enable_status_login_button(status=False)
