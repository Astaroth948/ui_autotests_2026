import allure
from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from testdata.text import ToolbarText
from ui_course.base_class import BaseClass
from ui_course.elements.button.button import Button
from ui_course.elements.text.text import Text


class CoursesListToolbar(BaseClass):
    def __init__(self, page: Page, step: str):
        super().__init__(page)

        self.substep: str = AllureSubstep.TOOLBAR
        self.step = self.generate_step(step=step)

        self.title = Text(
            page=page, locator='courses-list-toolbar-title-text', name=f'Заголовок ({self.substep})', step=self.step
        )
        self.create_course_button = Button(
            page=page,
            locator='courses-list-toolbar-create-course-button',
            name=f'Create course ({self.substep})',
            step=self.step,
        )

    def check_visible_status_toolbar(self, status: bool = True):
        with allure.step(
            '{step}Проверить {status} заголовка "{title}" и кнопки "Create course"'.format(
                step=self.step, status='отображение' if status else 'отсутствие', title=ToolbarText.COURSES_TITLE
            )
        ):
            self.title.check.visible_status(status=status)
            self.create_course_button.check.visible_status(status=status)
            if status:
                self.title.check.have_text(text=ToolbarText.COURSES_TITLE)

    def click_create_course_button(self):
        with allure.step(f'{self.step}Нажать на кнопку "Create course"'):
            self.create_course_button.action.click()
