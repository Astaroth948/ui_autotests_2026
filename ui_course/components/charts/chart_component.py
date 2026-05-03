import allure
from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from ui_course.base_class import BaseClass
from ui_course.elements.image.image import Image
from ui_course.elements.text.text import Text


class ChartComponent(BaseClass):
    def __init__(self, page: Page, identifier: str, chart_type: str, step: str):
        super().__init__(page)

        self.substep: str = AllureSubstep.CHARTS
        self.step = self.generate_step(step=step)

        self.title = Text(
            page=page, locator=f'{identifier}-widget-title-text', name=f'Заголовок ({self.substep})', step=self.step
        )
        self.chart = Image(page=page, locator=f'{identifier}-{chart_type}-chart', name=self.substep, step=self.step)

    def check_visible(self, title: str):
        with allure.step(f'{self.step}Проверить отображение графика "{title}"'):
            self.title.check.visible_status(status=True)
            self.title.check.have_text(text=title)

            self.chart.check.visible_status(status=True)
