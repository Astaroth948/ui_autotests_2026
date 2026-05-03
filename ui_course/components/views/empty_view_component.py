import allure
from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from ui_course.base_class import BaseClass
from ui_course.elements.icon.icon import Icon
from ui_course.elements.text.text import Text


class EmptyViewComponent(BaseClass):
    def __init__(self, page: Page, identifier: str, step: str):
        super().__init__(page)

        self.substep: str = AllureSubstep.EMPTY_VIEW
        self.step = self.generate_step(step=step)

        self.icon = Icon(page=page, locator=f'{identifier}-empty-view-icon', name=self.substep, step=self.step)
        self.title = Text(
            page=page, locator=f'{identifier}-empty-view-title-text', name=f'Title {self.substep}', step=self.step
        )
        self.description = Text(
            page=page,
            locator=f'{identifier}-empty-view-description-text',
            name=f'Description {self.substep}',
            step=self.step,
        )

    def check_visible_status(self, status=True, title: str | None = None, description: str | None = None):
        with allure.step(
            '{step}Проверить {visible_status} компонента Empty View'.format(
                step=self.step, visible_status='отображение' if status else 'отсутствие'
            )
        ):
            self.icon.check.visible_status(status=status)
            self.title.check.visible_status(status=status)
            self.description.check.visible_status(status=status)

            if status:
                self.title.check.have_text(text=title)
                self.description.check.have_text(text=description)
