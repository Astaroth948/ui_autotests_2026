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
@pytest.mark.smoke
@allure.epic(AllureEpic.COURSES)
@allure.parent_suite(AllureEpic.COURSES)
@allure.feature(AllureFeature.FUNCTIONAL)
@allure.suite(AllureFeature.FUNCTIONAL)
@allure.story(AllureStory.STORY)
@allure.sub_suite(AllureStory.STORY)
class TestFunctionalUserStoryCourses:
    @allure.severity(Severity.CRITICAL)
    @allure.title('Проверка создания, редактирования и удаления курсов')
    def test_create_edit_and_delete_course(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.delete_course(index=0)
        courses_page_with_courses.create_course(course_data=CourseEditorData.COURSE_HTTPX)
        courses_page_with_courses.edit_course(index=1, course_data=CourseEditorData.COURSE_PYTEST)

        courses_page_with_courses.list.check_courses_cards(
            cards_list=[
                CourseEditorData.COURSE_PLAYWRIGHT.main_form,
                CourseEditorData.COURSE_PYTEST.main_form,
                CourseEditorData.COURSE_HTTPX.main_form,
            ]
        )
