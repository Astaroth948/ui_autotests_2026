import allure
import pytest
from allure_commons.types import Severity

from testdata.allure.epics import AllureEpic
from testdata.allure.features import AllureFeature
from testdata.allure.stories import AllureStory
from testdata.courses import CourseEditorData
from testdata.routes import AppRoute
from ui_course.pages.courses.courses_page import CoursesPage


@pytest.mark.functional
@pytest.mark.courses
@pytest.mark.regression
@allure.epic(AllureEpic.COURSES)
@allure.parent_suite(AllureEpic.COURSES)
@allure.feature(AllureFeature.FUNCTIONAL)
@allure.suite(AllureFeature.FUNCTIONAL)
@allure.story(AllureStory.CREATE)
@allure.sub_suite(AllureStory.CREATE)
class TestFunctionalCreateCourses:
    @allure.severity(Severity.CRITICAL)
    @allure.title('Проверка создания курса')
    def test_create_course(self, courses_page_ignore_login: CoursesPage):
        courses_page_ignore_login.visit(url=AppRoute.COURSES)

        courses_page_ignore_login.create_course(course_data=CourseEditorData.COURSE_PYTHON)
        courses_page_ignore_login.list.check_visible_status_empty_view(status=False)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка отмены создания курса')
    def test_cancel_create_course(self, courses_page_ignore_login: CoursesPage):
        courses_page_ignore_login.visit(url=AppRoute.CREATE_COURSE)

        courses_page_ignore_login.editor.fill_course(course_data=CourseEditorData.COURSE_PYTHON)
        courses_page_ignore_login.sidebar.click_courses_button()

        courses_page_ignore_login.list.card.check_quantity_courses(count=0)
        courses_page_ignore_login.list.check_visible_status_empty_view(status=True)
