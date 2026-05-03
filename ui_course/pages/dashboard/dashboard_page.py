import allure
from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from testdata.text import ChartsText
from ui_course.components.navigation.header_component import HeaderComponent
from ui_course.components.navigation.sidebar_component import SidebarComponent
from ui_course.pages.base_page import BasePage
from ui_course.pages.dashboard.components.charts import DashboardCharts
from ui_course.pages.dashboard.components.toolbar import DashboardToolbar


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.substep: str = AllureSubstep.DASHBOARD
        self.step = self.generate_step(step=None)

        self.header = HeaderComponent(page=page, step=self.step)
        self.sidebar = SidebarComponent(page=page, step=self.step)
        self.chart = DashboardCharts(page=page, step=self.step)
        self.toolbar = DashboardToolbar(page=page, step=self.step)

    def check_visible_status_base_components(self, status: bool, username: str | None):
        with allure.step(
            '{step}Проверить {status} основных компонентов страницы Dashboard: Toolbar, Header, Sidebar'.format(
                step=self.step, status='отображение' if status else 'отсутствие'
            )
        ):
            self.toolbar.check_visible_status(status=status)
            self.header.check_visible_status(status=status, username=username)
            self.sidebar.check_visible_status(status=status)

    def check_visible_students_chart(self):
        self.chart.students.check_visible(title=ChartsText.STUDENTS)

    def check_visible_courses_chart(self):
        self.chart.courses.check_visible(title=ChartsText.COURSES)

    def check_visible_activities_chart(self):
        self.chart.activities.check_visible(title=ChartsText.ACTIVITIES)

    def check_visible_scores_chart(self):
        self.chart.scores.check_visible(title=ChartsText.SCORES)
