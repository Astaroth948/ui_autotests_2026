import allure
from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from testdata.text import HeaderText
from ui_course.base_class import BaseClass
from ui_course.elements.text.text import Text


class HeaderComponent(BaseClass):
    def __init__(self, page: Page, step: str):
        super().__init__(page)

        self.substep: str = AllureSubstep.HEADER
        self.step = self.generate_step(step=step)

        self.app_title = Text(page=page, locator='navigation-navbar-app-title-text', name='App title', step=self.step)
        self.welcome_title = Text(
            page=page, locator='navigation-navbar-welcome-title-text', name='Welcome title', step=self.step
        )

    def check_visible_status(self, status: bool = True, username: str | None = None):
        with allure.step(
            '{step}Проверить {status} общего элемента Header'.format(
                step=self.step, status='отображение' if status else 'отсутствие'
            )
        ):
            self.app_title.check.visible_status(status=status)
            self.welcome_title.check.visible_status(status=status)

            if status and username is not None:
                self.app_title.check.have_text(text=HeaderText.APP_TITLE)
                self.welcome_title.check.have_text(text=HeaderText.WELCOME_TITLE.format(username=username))
