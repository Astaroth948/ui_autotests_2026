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
@allure.issue('https://jira.example/browse/UI-1', name='UI-1')
@allure.epic(AllureEpic.COURSES)
@allure.parent_suite(AllureEpic.COURSES)
@allure.feature(AllureFeature.FAILED)
@allure.suite(AllureFeature.FAILED)
@allure.story(AllureStory.CUSTOM_REPORT)
@allure.sub_suite(AllureStory.CUSTOM_REPORT)
class TestFailedFunctionCustomReport:
    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения в теле самого теста (Custom Report)')
    def test_failed_call_body_custom_report(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.toolbar.click_create_course_button()
        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.editor.toolbar.check_visible_status_create_mode_title(status=True)
        assert 0
        courses_page_with_courses.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения setup фикстуры со скоупом function (Custom Report)')
    @pytest.mark.usefixtures('failed_fixture_setup')
    def test_failed_setup_function_custom_report(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.toolbar.click_create_course_button()

        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.editor.toolbar.check_visible_status_create_mode_title(status=True)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения teardown фикстуры со скоупом function (Custom Report)')
    @pytest.mark.usefixtures('failed_fixture_teardown')
    def test_failed_teardown_function_custom_report(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.toolbar.click_create_course_button()

        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.editor.toolbar.check_visible_status_create_mode_title(status=True)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения setup и teardown фикстур со скоупом function (Custom Report)')
    @pytest.mark.usefixtures('failed_fixture_setup')
    @pytest.mark.usefixtures('failed_fixture_teardown')
    def test_failed_setup_and_teardown_function_custom_report(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.toolbar.click_create_course_button()

        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.editor.toolbar.check_visible_status_create_mode_title(status=True)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения в теле теста и teardown фикстуры со скоупом function (Custom Report)')
    @pytest.mark.usefixtures('failed_fixture_teardown')
    def test_failed_call_body_and_teardown_function_custom_report(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.toolbar.click_create_course_button()

        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.editor.toolbar.check_visible_status_create_mode_title(status=True)
        assert 0
        courses_page_with_courses.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)


@pytest.mark.failed_session
@allure.issue('https://jira.example/browse/UI-2', name='UI-2')
@allure.epic(AllureEpic.COURSES)
@allure.parent_suite(AllureEpic.COURSES)
@allure.feature(AllureFeature.FAILED)
@allure.suite(AllureFeature.FAILED)
@allure.story(AllureStory.CUSTOM_REPORT)
@allure.sub_suite(AllureStory.CUSTOM_REPORT)
class TestFailedSetupSessionCustomReport:
    @pytest.mark.failed_session
    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения setup фикстуры со скоупом session (Custom Report)')
    def test_failed_setup_session_custom_report(self, courses_page_failed: CoursesPage):
        courses_page_failed.visit(url=AppRoute.COURSES)

        courses_page_failed.list.toolbar.click_create_course_button()

        courses_page_failed.check_visible_status_base_components(status=True, username=UsersData.DEFAULT_USER.username)
        courses_page_failed.editor.toolbar.check_visible_status_create_mode_title(status=True)


@pytest.mark.failed_class
@allure.issue('https://jira.example/browse/UI-3', name='UI-3')
@allure.epic(AllureEpic.COURSES)
@allure.parent_suite(AllureEpic.COURSES)
@allure.feature(AllureFeature.FAILED)
@allure.suite(AllureFeature.FAILED)
@allure.story(AllureStory.CUSTOM_REPORT)
@allure.sub_suite(AllureStory.CUSTOM_REPORT)
@pytest.mark.usefixtures('failed_fixture_setup_class')
class TestFailedSetupClassCustomReport:
    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения setup фикстуры со скоупом class (1) (Custom Report)')
    def test_failed_setup_class_1_custom_report(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.toolbar.click_create_course_button()
        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.editor.toolbar.check_visible_status_create_mode_title(status=True)
        courses_page_with_courses.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения setup фикстуры со скоупом class (2) (Custom Report)')
    def test_failed_setup_class_2_custom_report(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.toolbar.click_create_course_button()
        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.editor.toolbar.check_visible_status_create_mode_title(status=True)
        courses_page_with_courses.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения setup фикстуры со скоупом class (3) (Custom Report)')
    def test_failed_setup_class_3_custom_report(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.toolbar.click_create_course_button()
        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.editor.toolbar.check_visible_status_create_mode_title(status=True)
        courses_page_with_courses.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)


@pytest.mark.failed_module
@allure.issue('https://jira.example/browse/UI-3', name='UI-4')
@allure.epic(AllureEpic.COURSES)
@allure.parent_suite(AllureEpic.COURSES)
@allure.feature(AllureFeature.FAILED)
@allure.suite(AllureFeature.FAILED)
@allure.story(AllureStory.CUSTOM_REPORT)
@allure.sub_suite(AllureStory.CUSTOM_REPORT)
@pytest.mark.usefixtures('failed_fixture_setup_module')
class TestFailedSetupModuleCustomReport:
    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения setup фикстуры со скоупом module (1) (Custom Report)')
    def test_failed_setup_module_1_custom_report(self, courses_page_from_module: CoursesPage):
        courses_page_from_module.visit(url=AppRoute.COURSES)

        courses_page_from_module.list.toolbar.click_create_course_button()
        courses_page_from_module.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_from_module.editor.toolbar.check_visible_status_create_mode_title(status=True)
        courses_page_from_module.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения setup фикстуры со скоупом module (2) (Custom Report)')
    def test_failed_setup_module_2_custom_report(self, courses_page_from_module: CoursesPage):
        courses_page_from_module.visit(url=AppRoute.COURSES)

        courses_page_from_module.list.toolbar.click_create_course_button()
        courses_page_from_module.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_from_module.editor.toolbar.check_visible_status_create_mode_title(status=True)
        courses_page_from_module.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка падения setup фикстуры со скоупом module (3) (Custom Report)')
    def test_failed_setup_module_3_custom_report(self, courses_page_from_module: CoursesPage):
        courses_page_from_module.visit(url=AppRoute.COURSES)

        courses_page_from_module.list.toolbar.click_create_course_button()
        courses_page_from_module.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_from_module.editor.toolbar.check_visible_status_create_mode_title(status=True)
        courses_page_from_module.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)


@pytest.mark.fixed_function
@allure.issue('https://jira.example/browse/UI-1', name='UI-1')
@allure.epic(AllureEpic.COURSES)
@allure.parent_suite(AllureEpic.COURSES)
@allure.feature(AllureFeature.FAILED)
@allure.suite(AllureFeature.FAILED)
@allure.story(AllureStory.CUSTOM_REPORT)
@allure.sub_suite(AllureStory.CUSTOM_REPORT)
class TestFixedFunctionCustomReport:
    @allure.severity(Severity.NORMAL)
    @allure.issue('https://jira.example/browse/UI-6', name='UI-6')
    @allure.title('Проверка исправленного бага (1)')
    def test_fixed_bug_1_custom_report(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.toolbar.click_create_course_button()
        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.editor.toolbar.check_visible_status_create_mode_title(status=True)
        courses_page_with_courses.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)

    @allure.severity(Severity.NORMAL)
    @allure.issue('https://jira.example/browse/UI-6', name='UI-6')
    @allure.issue('https://jira.example/browse/UI-7', name='UI-7')
    @allure.title('Проверка исправленного бага (2)')
    def test_fixed_bug_2_custom_report(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.toolbar.click_create_course_button()
        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.editor.toolbar.check_visible_status_create_mode_title(status=True)
        courses_page_with_courses.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка исправленного бага (3)')
    def test_fixed_bug_3_custom_report(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.toolbar.click_create_course_button()
        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.editor.toolbar.check_visible_status_create_mode_title(status=True)
        courses_page_with_courses.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)
