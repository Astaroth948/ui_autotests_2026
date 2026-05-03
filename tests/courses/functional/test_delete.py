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
@allure.story(AllureStory.DELETE)
@allure.sub_suite(AllureStory.DELETE)
class TestFunctionalDeleteCourses:
    @allure.severity(Severity.CRITICAL)
    @allure.title('Проверка удаления курса')
    def test_delete_course(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.check_courses_cards(cards_list=PRECONDITION_COURSES_LIST)
        courses_page_with_courses.delete_course(index=1)
        courses_page_with_courses.list.check_courses_cards(
            cards_list=[CourseEditorData.COURSE_PYTHON.main_form, CourseEditorData.COURSE_SELENIUM.main_form]
        )

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка отмены удаления курса')
    @pytest.mark.parametrize('button_x', [pytest.param(True, id='X'), pytest.param(False, id='Cancel')])
    def test_cancel_delete_course(self, courses_page_with_courses: CoursesPage, button_x: bool):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.check_courses_cards(cards_list=PRECONDITION_COURSES_LIST)
        count_courses = courses_page_with_courses.list.card.get_quantity_courses()

        courses_page_with_courses.list.card.menu.click_delete_button(index=1)
        courses_page_with_courses.list.check_visible_status_delete_course_modal(status=True)

        if button_x:
            courses_page_with_courses.list.modal.click_x_button()
        else:
            courses_page_with_courses.list.modal.click_cancel_button()
        courses_page_with_courses.list.check_visible_status_delete_course_modal(status=False)

        courses_page_with_courses.list.card.check_quantity_courses(count=count_courses)
        courses_page_with_courses.list.check_courses_cards(cards_list=PRECONDITION_COURSES_LIST)
