import allure
import pytest
from allure_commons.types import Severity

from testdata.allure.epics import AllureEpic
from testdata.allure.features import AllureFeature
from testdata.allure.stories import AllureStory
from testdata.routes import AppRoute
from testdata.users import UsersData
from ui_course.pages.courses.courses_page import CoursesPage


@pytest.mark.view
@pytest.mark.courses
@pytest.mark.regression
@allure.epic(AllureEpic.COURSES)
@allure.parent_suite(AllureEpic.COURSES)
@allure.feature(AllureFeature.VIEW)
@allure.suite(AllureFeature.VIEW)
@allure.story(AllureStory.COURSES_LIST)
@allure.sub_suite(AllureStory.COURSES_LIST)
class TestViewCoursesList:
    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка отображения компонента "Empty View" страницы списка курсов без созданных курсов')
    def test_empty_courses_list_default(self, courses_page_ignore_login: CoursesPage):
        courses_page_ignore_login.visit(url=AppRoute.COURSES)

        courses_page_ignore_login.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_ignore_login.list.toolbar.check_visible_status_toolbar(status=True)
        courses_page_ignore_login.list.check_visible_status_empty_view(status=True)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка отображения компонента "Empty View" страницы списка курсов при удалении всех курсов')
    def test_empty_courses_list_when_delete_all_courses(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.check_visible_status_empty_view(status=False)
        count_courses = courses_page_with_courses.list.card.get_quantity_courses()

        for index in range(count_courses, 0, -1):
            courses_page_with_courses.delete_course(index=index - 1)

        courses_page_with_courses.list.check_visible_status_empty_view(status=True)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка отображения модального окна при удалении курса')
    def test_status_modal_when_delete_course(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.check_visible_status_delete_course_modal(status=False)
        courses_page_with_courses.list.card.menu.click_delete_button(index=0)
        courses_page_with_courses.list.check_visible_status_delete_course_modal(status=True)
        courses_page_with_courses.list.modal.click_confirm_button()
        courses_page_with_courses.list.check_visible_status_delete_course_modal(status=False)
