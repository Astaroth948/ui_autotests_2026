import allure
from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from ui_course.pages.authentication.components.alerts import AuthAlerts
from ui_course.pages.authentication.components.header import AuthHeader
from ui_course.pages.authentication.components.login_form import LoginForm
from ui_course.pages.authentication.components.reg_form import RegistrationForm
from ui_course.pages.authentication.components.toolbar import AuthToolbar
from ui_course.pages.authentication.models import UserModel
from ui_course.pages.base_page import BasePage


class AuthPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.substep: str = AllureSubstep.AUTHENTICATION
        self.step = self.generate_step(step=None)

        self.alerts = AuthAlerts(page=page, step=self.step)
        self.header = AuthHeader(page=page, step=self.step)
        self.login_form = LoginForm(page=page, step=self.step)
        self.reg_form = RegistrationForm(page=page, step=self.step)
        self.toolbar = AuthToolbar(page=page, step=self.step)

    def registration_user(self, user_data: UserModel):
        with allure.step(f'{self.step}Зарегистрировать пользователя: "{user_data}"'):
            self.header.check_visible_status_header(status=True)
            self.toolbar.check_registration_mode()
            self.reg_form.fill(user_data=user_data)
            self.toolbar.check_enable_status_registration_button(status=True)
            self.toolbar.click_registration_button()
            self.header.check_visible_status_header(status=False)

    def login_user(self, user_data: UserModel):
        with allure.step(f'{self.step}Авторизоваться пользователем: "{user_data}"'):
            self.header.check_visible_status_header(status=True)
            self.toolbar.check_login_mode()
            self.login_form.fill(user_data=user_data)
            self.toolbar.check_enable_status_login_button(status=True)
            self.toolbar.click_login_button()
            self.header.check_visible_status_header(status=False)
