import allure
import pytest
from allure_commons.types import Severity

from testdata.allure.epics import AllureEpic
from testdata.allure.features import AllureFeature
from testdata.allure.stories import AllureStory
from testdata.courses import CourseEditorData, CourseExercisesFormData
from testdata.routes import AppRoute
from testdata.users import UsersData
from ui_course.pages.courses.courses_page import CoursesPage
from ui_course.pages.courses.models import CourseEditorMainFormModel


@pytest.mark.view
@pytest.mark.courses
@pytest.mark.regression
@allure.epic(AllureEpic.COURSES)
@allure.parent_suite(AllureEpic.COURSES)
@allure.feature(AllureFeature.VIEW)
@allure.suite(AllureFeature.VIEW)
@allure.story(AllureStory.COURSE_EDITOR)
@allure.sub_suite(AllureStory.COURSE_EDITOR)
class TestViewCourseEditor:
    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка отображения дефолтных данных при создании курса')
    def test_default_values_when_create_course(self, courses_page_ignore_login: CoursesPage):
        courses_page_ignore_login.visit(url=AppRoute.CREATE_COURSE)

        courses_page_ignore_login.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_ignore_login.editor.toolbar.check_visible_status_toolbar(status=True)
        courses_page_ignore_login.editor.toolbar.check_visible_status_create_mode_title(status=True)
        courses_page_ignore_login.editor.toolbar.check_enable_status_create_course_button(status=False)
        courses_page_ignore_login.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)
        courses_page_ignore_login.editor.check_filling_course(course_data=CourseEditorData.COURSE_EMPTY)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка отображения корректных данных при редактировании курса')
    def test_correct_values_when_edit_course(self, courses_page_with_courses: CoursesPage):
        courses_page_with_courses.visit(url=AppRoute.COURSES)

        courses_page_with_courses.list.card.menu.click_edit_button(index=0)
        courses_page_with_courses.check_visible_status_base_components(
            status=True, username=UsersData.DEFAULT_USER.username
        )
        courses_page_with_courses.editor.toolbar.check_visible_status_toolbar(status=True)
        courses_page_with_courses.editor.toolbar.check_visible_status_edit_mode_title(status=True)
        courses_page_with_courses.editor.toolbar.check_enable_status_create_course_button(status=True)
        courses_page_with_courses.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=True)
        courses_page_with_courses.editor.check_filling_course(course_data=CourseEditorData.COURSE_PYTHON)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка состояния "Image Upload Widget" при загрузке и удалении изображения')
    def test_status_image_upload_widget_when_upload_and_remove_image(self, courses_page_ignore_login: CoursesPage):
        courses_page_ignore_login.visit(url=AppRoute.CREATE_COURSE)

        courses_page_ignore_login.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)
        courses_page_ignore_login.editor.image_upload_widget.upload_preview_image(
            file=CourseEditorData.COURSE_PYTHON.image_file
        )
        courses_page_ignore_login.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=True)
        courses_page_ignore_login.editor.image_upload_widget.click_remove_image_button()
        courses_page_ignore_login.editor.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка состояния активности кнопки "Create course" при загрузке и удалении изображения')
    def test_status_create_course_button_when_upload_and_remove_image(self, courses_page_ignore_login: CoursesPage):
        courses_page_ignore_login.visit(url=AppRoute.CREATE_COURSE)

        courses_page_ignore_login.editor.fill_course(course_data=CourseEditorData.COURSE_PYTHON)
        courses_page_ignore_login.editor.toolbar.check_enable_status_create_course_button(status=True)

        courses_page_ignore_login.editor.image_upload_widget.click_remove_image_button()
        courses_page_ignore_login.editor.toolbar.check_enable_status_create_course_button(status=False)

        courses_page_ignore_login.editor.image_upload_widget.upload_preview_image(
            file=CourseEditorData.COURSE_PLAYWRIGHT.image_file
        )
        courses_page_ignore_login.editor.toolbar.check_enable_status_create_course_button(status=True)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка состояния активности кнопки "Create course" при некорректном заполнении обязательных полей')
    @pytest.mark.parametrize(
        'incorrect_form_data',
        [
            pytest.param({'course_title': ''}),
            pytest.param({'estimated_time': ''}),
            pytest.param({'description': ''}),
            pytest.param({'max_score': '0'}),
            pytest.param({'min_score': '0'}),
        ],
    )
    def test_status_create_course_button_when_incorrect_filling_required_fields(
        self, courses_page_ignore_login: CoursesPage, incorrect_form_data: dict
    ):
        courses_page_ignore_login.visit(url=AppRoute.CREATE_COURSE)

        courses_page_ignore_login.editor.fill_course(course_data=CourseEditorData.COURSE_PYTHON)
        courses_page_ignore_login.editor.toolbar.check_enable_status_create_course_button(status=True)

        form_data_dict = CourseEditorData.COURSE_PYTHON.main_form.model_dump()
        form_data_dict.update(incorrect_form_data)
        form_data = CourseEditorMainFormModel(**form_data_dict)

        courses_page_ignore_login.editor.main_form.fill(form_data=form_data)
        courses_page_ignore_login.editor.toolbar.check_enable_status_create_course_button(status=False)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка состояния компонента "Empty View" при добавлении и удалении элементов раздела "Exercises"')
    def test_status_empty_view_when_add_and_remove_exercises(self, courses_page_ignore_login: CoursesPage):
        courses_page_ignore_login.visit(url=AppRoute.CREATE_COURSE)

        courses_page_ignore_login.editor.exercise_form.check_visible_status_exercises_empty_view(status=True)
        courses_page_ignore_login.editor.toolbar.click_create_exercise_button()
        courses_page_ignore_login.editor.exercise_form.check_visible_status_exercises_empty_view(status=False)
        courses_page_ignore_login.editor.toolbar.click_delete_exercise_button(index=0)
        courses_page_ignore_login.editor.exercise_form.check_visible_status_exercises_empty_view(status=True)

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка дефолтных значений новых элементов раздела "Exercises"')
    def test_default_values_exercises(self, courses_page_ignore_login: CoursesPage):
        courses_page_ignore_login.visit(url=AppRoute.CREATE_COURSE)

        count_exercises = 5
        courses_page_ignore_login.editor.toolbar.set_quantity_exercises(count=count_exercises)
        for index in range(count_exercises):
            courses_page_ignore_login.editor.exercise_form.check_filling(
                index=index, form_data=CourseExercisesFormData.DEFAULT_EXERCISE_FORM
            )
