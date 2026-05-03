import allure
from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from ui_course.base_class import BaseClass
from ui_course.elements.button.button import Button
from ui_course.elements.link.link import Link


class AuthToolbar(BaseClass):
    def __init__(self, page: Page, step: str):
        super().__init__(page)

        self.substep: str = AllureSubstep.TOOLBAR
        self.step = self.generate_step(step=step)

        self.login_button = Button(
            page=page, locator='login-page-login-button', name=f'Login ({self.substep})', step=self.step
        )
        self.login_link = Link(
            page=page, locator='registration-page-login-link', name=f'Login ({self.substep})', step=self.step
        )
        self.registration_button = Button(
            page=page,
            locator='registration-page-registration-button',
            name=f'Registration ({self.substep})',
            step=self.step,
        )
        self.registration_link = Link(
            page=page, locator='login-page-registration-link', name=f'Registration ({self.substep})', step=self.step
        )

    def click_login_button(self):
        with allure.step(f'{self.step}Нажать на кнопку "Login"'):
            self.login_button.action.click()

    def click_login_link(self):
        with allure.step(f'{self.step}Нажать на ссылку "Login"'):
            self.login_link.action.click()

    def click_registration_link(self):
        with allure.step(f'{self.step}Нажать на ссылку "Registration"'):
            self.registration_link.action.click()

    def click_registration_button(self):
        with allure.step(f'{self.step}Нажать на кнопку "Registration"'):
            self.registration_button.action.click()

    def check_login_mode(self):
        with allure.step(f'{self.step}Проверить отображение кнопки "Login" и ссылки "Registration"'):
            self.login_button.check.visible_status(status=True)
            self.login_link.check.visible_status(status=False)
            self.registration_button.check.visible_status(status=False)
            self.registration_link.check.visible_status(status=True)

    def check_registration_mode(self):
        with allure.step(f'{self.step}Проверить отображение кнопки "Registration" и ссылки "Login"'):
            self.login_button.check.visible_status(status=False)
            self.login_link.check.visible_status(status=True)
            self.registration_button.check.visible_status(status=True)
            self.registration_link.check.visible_status(status=False)

    def check_enable_status_login_button(self, status: bool = True):
        with allure.step(
            '{step}Проверить состояние {status} кнопки "Login"'.format(
                step=self.step, status='enabled' if status else 'disabled'
            )
        ):
            self.login_button.check.enable_status(status=status)

    def check_enable_status_registration_button(self, status: bool = True):
        with allure.step(
            '{step}Проверить состояние {status} кнопки "Registration"'.format(
                step=self.step, status='enabled' if status else 'disabled'
            )
        ):
            self.registration_button.check.enable_status(status=status)
