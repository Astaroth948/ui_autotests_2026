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
@allure.story(AllureStory.REGISTRATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestViewRegistration:
    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка дефолтного состояния страницы регистрации')
    def test_default_state_registration_page(self, auth_page: AuthPage):
        auth_page.visit(url=AppRoute.REGISTRATION)

        auth_page.header.check_visible_status_header(status=True)
        auth_page.toolbar.check_registration_mode()
        auth_page.reg_form.check_filling(user_data=UsersData.EMPTY_FORM)
        auth_page.toolbar.check_enable_status_registration_button(status=False)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка состояния активности кнопки "Registration" при заполнении некорректных данных пользователя')
    @pytest.mark.parametrize(
        'incorrect_user_data',
        [
            pytest.param({'email': ''}),
            pytest.param({'username': ''}, marks=pytest.mark.skip(reason="Не работает")),
            pytest.param({'password': ''}),
        ],
    )
    def test_status_registration_button_when_filling_incorrect_user_data(
        self, auth_page: AuthPage, incorrect_user_data: dict
    ):
        auth_page.visit(url=AppRoute.REGISTRATION)

        auth_page.reg_form.fill(user_data=UsersData.DEFAULT_USER)
        auth_page.toolbar.check_enable_status_registration_button(status=True)

        user_data_dict = UsersData.DEFAULT_USER.model_dump()
        user_data_dict.update(incorrect_user_data)
        user_data = IncorrectUserModel(**user_data_dict)

        auth_page.reg_form.fill(user_data=user_data)
        auth_page.toolbar.check_enable_status_registration_button(status=False)
