import allure
import pytest
from allure_commons.types import Severity

from testdata.allure.epics import AllureEpic
from testdata.allure.features import AllureFeature
from testdata.allure.stories import AllureStory
from testdata.courses import CourseEditorData
from testdata.routes import AppRoute
from testdata.users import UsersData
from ui_course.pages.courses.courses_page import CoursesPage


@pytest.mark.navigation
@pytest.mark.courses
@pytest.mark.regression
@allure.epic(AllureEpic.COURSES)
@allure.parent_suite(AllureEpic.COURSES)
@allure.feature(AllureFeature.NAVIGATION)
@allure.suite(AllureFeature.NAVIGATION)
@allure.story(AllureStory.LINKED_PAGES)
@allure.sub_suite(AllureStory.LINKED_PAGES)
class TestNavigationCourses:
    @allure.severity(Severity.NORMAL)
    @allure.title(
        'Проверка перехода со страницы списка курсов на страницу редактора при нажатии на кнопку "Create course"'
    )
    def test_navigation_from_courses_list_to_editor_when_click_create_course_button(
        self, courses_page_ignore_login: CoursesPage
    ):
        courses_page_ignore_login.visit(url=AppRoute.COURSES)
        courses_page_ignore_login.check_current_url(expected_url=AppRoute.COURSES)
        courses_page_ignore_login.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_ignore_login.list.toolbar.check_visible_status_toolbar(status=True)
        courses_page_ignore_login.editor.toolbar.check_visible_status_toolbar(status=False)
        courses_page_ignore_login.editor.toolbar.check_visible_status_create_mode_title(status=False)

        courses_page_ignore_login.list.toolbar.click_create_course_button()

        courses_page_ignore_login.check_current_url(expected_url=AppRoute.CREATE_COURSE)
        courses_page_ignore_login.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_ignore_login.list.toolbar.check_visible_status_toolbar(status=False)
        courses_page_ignore_login.editor.toolbar.check_visible_status_toolbar(status=True)
        courses_page_ignore_login.editor.toolbar.check_visible_status_create_mode_title(status=True)

    @allure.severity(Severity.NORMAL)
    @allure.title(
        'Проверка перехода со страницы редактора (создание) на страницу списка курсов при нажатии на кнопку "Create course"'
    )
    def test_navigation_from_editor_create_mode_to_courses_list_when_click_create_course_button(
        self, courses_page_ignore_login: CoursesPage
    ):
        courses_page_ignore_login.visit(url=AppRoute.CREATE_COURSE)
        courses_page_ignore_login.check_current_url(expected_url=AppRoute.CREATE_COURSE)
        courses_page_ignore_login.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_ignore_login.list.toolbar.check_visible_status_toolbar(status=False)
        courses_page_ignore_login.editor.toolbar.check_visible_status_toolbar(status=True)
        courses_page_ignore_login.editor.toolbar.check_visible_status_create_mode_title(status=True)

        courses_page_ignore_login.editor.image_upload_widget.upload_preview_image(
            file=CourseEditorData.COURSE_PYTHON.image_file
        )
        courses_page_ignore_login.editor.main_form.fill(form_data=CourseEditorData.COURSE_PYTHON.main_form)
        courses_page_ignore_login.editor.toolbar.click_create_course_button()

        courses_page_ignore_login.check_current_url(expected_url=AppRoute.COURSES)
        courses_page_ignore_login.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_ignore_login.list.toolbar.check_visible_status_toolbar(status=True)
        courses_page_ignore_login.editor.toolbar.check_visible_status_toolbar(status=False)
        courses_page_ignore_login.editor.toolbar.check_visible_status_create_mode_title(status=False)

    @allure.severity(Severity.NORMAL)
    @allure.title(
        'Проверка перехода со страницы редактора (редактирование) на страницу списка курсов при нажатии на кнопку "Create course"'
    )
    def test_navigation_from_editor_edit_mode_to_courses_list_when_click_create_course_button(
        self, courses_page_with_courses: CoursesPage
    ):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.card.menu.click_edit_button(index=1)
        courses_page_with_courses.check_current_url(expected_url=AppRoute.EDIT_COURSE)
        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.list.toolbar.check_visible_status_toolbar(status=False)
        courses_page_with_courses.editor.toolbar.check_visible_status_toolbar(status=True)
        courses_page_with_courses.editor.toolbar.check_visible_status_edit_mode_title(status=True)

        courses_page_with_courses.editor.toolbar.click_create_course_button()

        courses_page_with_courses.check_current_url(expected_url=AppRoute.COURSES)
        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.list.toolbar.check_visible_status_toolbar(status=True)
        courses_page_with_courses.editor.toolbar.check_visible_status_toolbar(status=False)
        courses_page_with_courses.editor.toolbar.check_visible_status_edit_mode_title(status=False)
