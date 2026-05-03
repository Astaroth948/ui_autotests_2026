import allure
from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from testdata.text import ToolbarText
from ui_course.base_class import BaseClass
from ui_course.elements.text.text import Text


class DashboardToolbar(BaseClass):
    def __init__(self, page: Page, step: str):
        super().__init__(page)

        self.substep: str = AllureSubstep.TOOLBAR
        self.step = self.generate_step(step=step)

        self.title = Text(page=page, locator='dashboard-toolbar-title-text', name='Title', step=self.step)

    def check_visible_status(self, status: bool = True):
        with allure.step(
            '{step}Проверить {status} тулбара "{title}"'.format(
                step=self.step, status='отображение' if status else 'отсутствие', title=ToolbarText.DASHBOARD_TITLE
            )
        ):
            self.title.check.visible_status(status=status)
            if status:
                self.title.check.have_text(text=ToolbarText.DASHBOARD_TITLE)
