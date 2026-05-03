import allure
import pytest
from allure_commons.types import Severity

from testdata.allure.epics import AllureEpic
from testdata.allure.features import AllureFeature
from testdata.allure.stories import AllureStory
from testdata.routes import AppRoute
from testdata.users import UsersData
from ui_course.pages.courses.courses_page import CoursesPage


@pytest.mark.failed_function
@allure.epic(AllureEpic.COURSES)
@allure.parent_suite(AllureEpic.COURSES)
@allure.feature(AllureFeature.FAILED)
@allure.suite(AllureFeature.FAILED)
@allure.story(AllureStory.FAILED)
@allure.sub_suite(AllureStory.FAILED)
class TestFailedFunction:
    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения в теле самого теста')
    def test_failed_call_body(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.toolbar.click_create_course_button()
        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.editor.toolbar.check_visible_status_create_mode_title(status=True)
        assert 0
        courses_page_with_courses.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения setup фикстуры со скоупом function')
    @pytest.mark.usefixtures('failed_fixture_setup')
    def test_failed_setup_function(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.toolbar.click_create_course_button()

        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.editor.toolbar.check_visible_status_create_mode_title(status=True)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения teardown фикстуры со скоупом function')
    @pytest.mark.usefixtures('failed_fixture_teardown')
    def test_failed_teardown_function(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.toolbar.click_create_course_button()

        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.editor.toolbar.check_visible_status_create_mode_title(status=True)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения setup и teardown фикстур со скоупом function')
    @pytest.mark.usefixtures('failed_fixture_setup')
    @pytest.mark.usefixtures('failed_fixture_teardown')
    def test_failed_setup_and_teardown_function(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.toolbar.click_create_course_button()

        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.editor.toolbar.check_visible_status_create_mode_title(status=True)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения в теле теста и teardown фикстуры со скоупом function')
    @pytest.mark.usefixtures('failed_fixture_teardown')
    def test_failed_call_body_and_teardown_function(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.toolbar.click_create_course_button()

        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.editor.toolbar.check_visible_status_create_mode_title(status=True)
        assert 0
        courses_page_with_courses.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)


@pytest.mark.failed_session
@allure.epic(AllureEpic.COURSES)
@allure.parent_suite(AllureEpic.COURSES)
@allure.feature(AllureFeature.FAILED)
@allure.suite(AllureFeature.FAILED)
@allure.story(AllureStory.FAILED)
@allure.sub_suite(AllureStory.FAILED)
class TestFailedSetupSession:
    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения setup фикстуры со скоупом session')
    def test_failed_setup_session(self, courses_page_failed: CoursesPage):
        courses_page_failed.visit(url=AppRoute.COURSES)

        courses_page_failed.list.toolbar.click_create_course_button()

        courses_page_failed.check_visible_status_base_components(status=True, username=UsersData.DEFAULT_USER.username)
        courses_page_failed.editor.toolbar.check_visible_status_create_mode_title(status=True)


@pytest.mark.failed_class
@allure.epic(AllureEpic.COURSES)
@allure.parent_suite(AllureEpic.COURSES)
@allure.feature(AllureFeature.FAILED)
@allure.suite(AllureFeature.FAILED)
@allure.story(AllureStory.FAILED)
@allure.sub_suite(AllureStory.FAILED)
@pytest.mark.usefixtures('failed_fixture_setup_class')
class TestFailedSetupClass:
    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения setup фикстуры со скоупом class (1)')
    def test_failed_setup_class_1(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.toolbar.click_create_course_button()
        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.editor.toolbar.check_visible_status_create_mode_title(status=True)
        courses_page_with_courses.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения setup фикстуры со скоупом class (2)')
    def test_failed_setup_class_2(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.toolbar.click_create_course_button()
        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.editor.toolbar.check_visible_status_create_mode_title(status=True)
        courses_page_with_courses.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения setup фикстуры со скоупом class (3)')
    def test_failed_setup_class_3(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.toolbar.click_create_course_button()
        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.editor.toolbar.check_visible_status_create_mode_title(status=True)
        courses_page_with_courses.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)


@pytest.mark.failed_module
@allure.epic(AllureEpic.COURSES)
@allure.parent_suite(AllureEpic.COURSES)
@allure.feature(AllureFeature.FAILED)
@allure.suite(AllureFeature.FAILED)
@allure.story(AllureStory.FAILED)
@allure.sub_suite(AllureStory.FAILED)
@pytest.mark.usefixtures('failed_fixture_setup_module')
class TestFailedSetupModule:
    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения setup фикстуры со скоупом module (1)')
    def test_failed_setup_module_1(self, courses_page_from_module: CoursesPage):
        courses_page_from_module.visit(url=AppRoute.COURSES)

        courses_page_from_module.list.toolbar.click_create_course_button()
        courses_page_from_module.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_from_module.editor.toolbar.check_visible_status_create_mode_title(status=True)
        courses_page_from_module.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения setup фикстуры со скоупом module (2)')
    def test_failed_setup_module_2(self, courses_page_from_module: CoursesPage):
        courses_page_from_module.visit(url=AppRoute.COURSES)

        courses_page_from_module.list.toolbar.click_create_course_button()
        courses_page_from_module.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_from_module.editor.toolbar.check_visible_status_create_mode_title(status=True)
        courses_page_from_module.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения setup фикстуры со скоупом module (3)')
    def test_failed_setup_module_3(self, courses_page_from_module: CoursesPage):
        courses_page_from_module.visit(url=AppRoute.COURSES)

        courses_page_from_module.list.toolbar.click_create_course_button()
        courses_page_from_module.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_from_module.editor.toolbar.check_visible_status_create_mode_title(status=True)
        courses_page_from_module.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)
