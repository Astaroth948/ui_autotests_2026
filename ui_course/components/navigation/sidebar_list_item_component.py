import allure
from playwright.sync_api import Page

from ui_course.base_class import BaseClass
from ui_course.elements.button.button import Button
from ui_course.elements.icon.icon import Icon
from ui_course.elements.text.text import Text


class SidebarListItemComponent(BaseClass):
    def __init__(self, page: Page, identifier: str, step: str):
        super().__init__(page)

        self.step = step

        self.icon = Icon(
            page=page, locator=f'{identifier}-drawer-list-item-icon', name=f'{identifier} (Sidebar)', step=self.step
        )
        self.title = Text(
            page=page,
            locator=f'{identifier}-drawer-list-item-title-text',
            name=f'{identifier} (Sidebar)',
            step=self.step,
        )
        self.button = Button(
            page=page, locator=f'{identifier}-drawer-list-item-button', name=f'{identifier} (Sidebar)', step=self.step
        )

    def check_visible_status(self, status: bool = True, title: str | None = None):
        with allure.step(
            '{step}Проверить {status} элемента сайдбара "{title}"'.format(
                step=self.step, status='отображение' if status else 'отсутствие', title=title
            )
        ):
            self.icon.check.visible_status(status=status)
            self.title.check.visible_status(status=status)
            self.button.check.visible_status(status=status)

            if status:
                self.title.check.have_text(text=title)
