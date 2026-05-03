import allure
from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from ui_course.base_class import BaseClass
from ui_course.elements.input.input import Input
from ui_course.pages.authentication.models import UserModel


class RegistrationForm(BaseClass):
    def __init__(self, page: Page, step: str):
        super().__init__(page)

        self.substep: str = AllureSubstep.REGISTRATION_FORM
        self.step = self.generate_step(step=step)

        self.email_input = Input(
            page=page, locator='registration-form-email-input', name=f'Email ({self.substep})', step=self.step
        )
        self.username_input = Input(
            page=page, locator='registration-form-username-input', name=f'Username ({self.substep})', step=self.step
        )
        self.password_input = Input(
            page=page, locator='registration-form-password-input', name=f'Password ({self.substep})', step=self.step
        )

    def fill(self, user_data: UserModel):
        with allure.step(f'{self.step}Заполнить форму данными: "{user_data}"'):
            self.email_input.action.fill(value=user_data.email)
            self.email_input.check.have_value(value=user_data.email)

            self.username_input.action.fill(value=user_data.username)
            self.username_input.check.have_value(value=user_data.username)

            self.password_input.action.fill(value=user_data.password)
            self.password_input.check.have_value(value=user_data.password)

    def check_filling(self, user_data: UserModel):
        with allure.step(f'{self.step}Проверить, что форма заполнена данными: "{user_data}"'):
            self.email_input.check.visible_status(status=True)
            self.email_input.check.have_value(value=user_data.email)

            self.username_input.check.visible_status(status=True)
            self.username_input.check.have_value(value=user_data.username)

            self.password_input.check.visible_status(status=True)
            self.password_input.check.have_value(value=user_data.password)
