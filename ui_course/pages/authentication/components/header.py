import allure
from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from testdata.text import HeaderText
from ui_course.base_class import BaseClass
from ui_course.elements.text.text import Text


class AuthHeader(BaseClass):
    def __init__(self, page: Page, step: str):
        super().__init__(page)

        self.substep: str = AllureSubstep.HEADER
        self.step = self.generate_step(step=step)

        self.title = Text(
            page=page, locator='authentication-ui-course-title-text', name=f'Заголовок ({self.substep})', step=self.step
        )

    def check_visible_status_header(self, status: bool = True):
        with allure.step(
            '{step}Проверить {status} элемента Header страницы Аутентификации'.format(
                step=self.step, status='отображение' if status else 'отсутствие'
            )
        ):
            self.title.check.visible_status(status=status)
            if status:
                self.title.check.have_text(text=HeaderText.APP_TITLE)
