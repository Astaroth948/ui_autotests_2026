import allure
import pytest
from allure_commons.types import Severity

from testdata.allure.epics import AllureEpic
from testdata.allure.features import AllureFeature
from testdata.allure.stories import AllureStory
from testdata.courses import PRECONDITION_COURSES_LIST, CourseEditorData
from testdata.routes import AppRoute
from ui_course.pages.courses.courses_page import CoursesPage


@pytest.mark.functional
@pytest.mark.courses
@pytest.mark.regression
@allure.epic(AllureEpic.COURSES)
@allure.parent_suite(AllureEpic.COURSES)
@allure.feature(AllureFeature.FUNCTIONAL)
@allure.suite(AllureFeature.FUNCTIONAL)
@allure.story(AllureStory.EDIT)
@allure.sub_suite(AllureStory.EDIT)
class TestFunctionalEditCourses:
    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка редактирования курса')
    def test_edit_course(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.check_courses_cards(cards_list=PRECONDITION_COURSES_LIST)
        courses_page_with_courses.edit_course(index=1, course_data=CourseEditorData.COURSE_HTTPX)
        courses_page_with_courses.list.check_courses_cards(
            cards_list=[
                CourseEditorData.COURSE_PYTHON.main_form,
                CourseEditorData.COURSE_HTTPX.main_form,
                CourseEditorData.COURSE_SELENIUM.main_form,
            ]
        )

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка отмены редактирования курса')
    def test_cancel_edit_course(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.check_courses_cards(cards_list=PRECONDITION_COURSES_LIST)

        courses_page_with_courses.list.card.menu.click_edit_button(index=1)
        courses_page_with_courses.editor.fill_course(course_data=CourseEditorData.COURSE_HTTPX)
        courses_page_with_courses.sidebar.click_courses_button()

        courses_page_with_courses.list.check_courses_cards(cards_list=PRECONDITION_COURSES_LIST)
