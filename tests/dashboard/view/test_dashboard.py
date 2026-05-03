import allure
import pytest
from allure_commons.types import Severity

from testdata.allure.epics import AllureEpic
from testdata.allure.features import AllureFeature
from testdata.allure.stories import AllureStory
from testdata.routes import AppRoute
from testdata.users import UsersData
from ui_course.pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.view
@pytest.mark.dashboard
@pytest.mark.regression
@allure.epic(AllureEpic.DASHBOARD)
@allure.parent_suite(AllureEpic.DASHBOARD)
@allure.feature(AllureFeature.VIEW)
@allure.suite(AllureFeature.VIEW)
@allure.story(AllureStory.DASHBOARD)
@allure.sub_suite(AllureStory.DASHBOARD)
class TestViewDashboard:
    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка отображения страницы Dashboard')
    def test_dashboard_displaying(self, dashboard_page_ignore_login: DashboardPage):
        dashboard_page_ignore_login.visit(url=AppRoute.DASHBOARD)

        dashboard_page_ignore_login.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )

        dashboard_page_ignore_login.check_visible_scores_chart()
        dashboard_page_ignore_login.check_visible_courses_chart()
        dashboard_page_ignore_login.check_visible_students_chart()
        dashboard_page_ignore_login.check_visible_activities_chart()
