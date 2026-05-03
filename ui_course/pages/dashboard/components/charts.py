from playwright.sync_api import Page

from ui_course.base_class import BaseClass
from ui_course.components.charts.chart_component import ChartComponent


class DashboardCharts(BaseClass):
    def __init__(self, page: Page, step: str):
        super().__init__(page)

        self.scores = ChartComponent(page=page, identifier='scores', chart_type='scatter', step=step)
        self.courses = ChartComponent(page=page, identifier='courses', chart_type='pie', step=step)
        self.students = ChartComponent(page=page, identifier='students', chart_type='bar', step=step)
        self.activities = ChartComponent(page=page, identifier='activities', chart_type='line', step=step)
