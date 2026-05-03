import allure
from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from ui_course.components.views.image_upload_widget_component import ImageUploadWidgetComponent
from ui_course.pages.base_page import BasePage
from ui_course.pages.courses.course_editor.components.exercise_form import CourseEditorExerciseForm
from ui_course.pages.courses.course_editor.components.main_form import CourseEditorMainForm
from ui_course.pages.courses.course_editor.components.toolbar import CourseEditorToolbar
from ui_course.pages.courses.models import CourseEditorExercisesFormModel, CourseEditorModel


class CourseEditorPage(BasePage):
    def __init__(self, page: Page, step: str):
        super().__init__(page)

        self.substep: str = AllureSubstep.CREATE_COURSE
        self.step = self.generate_step(step=step)

        self.image_upload_widget = ImageUploadWidgetComponent(
            page=page, identifier='create-course-preview', step=self.step
        )
        self.main_form = CourseEditorMainForm(page=page, step=self.step)
        self.exercise_form = CourseEditorExerciseForm(page=page, step=self.step)
        self.toolbar = CourseEditorToolbar(page=page, step=self.step)

    def fill_exercises(self, exercises_list: list[CourseEditorExercisesFormModel]):
        count_exercises = len(exercises_list)
        self.toolbar.set_quantity_exercises(count=count_exercises)
        if count_exercises:
            for exercise_data in exercises_list:
                self.exercise_form.fill(index=exercises_list.index(exercise_data), form_data=exercise_data)
        else:
            self.exercise_form.check_visible_status_exercises_empty_view(status=True)

    def fill_course(self, course_data: CourseEditorModel):
        with allure.step(f'{self.step}Заполнить курс данными: "{course_data}"'):
            if course_data.image_file is None:
                self.image_upload_widget.remove_preview_image()
                self.image_upload_widget.check_visible_status_widget(is_image_uploaded=False)
            else:
                self.image_upload_widget.upload_preview_image(file=course_data.image_file)
                self.image_upload_widget.check_visible_status_widget(is_image_uploaded=True)

            self.main_form.fill(form_data=course_data.main_form)
            self.fill_exercises(exercises_list=course_data.exercises_form)

    def check_filling_course(self, course_data: CourseEditorModel):
        with allure.step(f'{self.step}Проверить, что курс заполнен данными: "{course_data}"'):
            is_image_uploaded = True
            if course_data.image_file is None:
                is_image_uploaded = False
            self.image_upload_widget.check_visible_status_widget(is_image_uploaded=is_image_uploaded)

            self.main_form.check_filling(form_data=course_data.main_form)

            count_exercises = len(course_data.exercises_form)
            if count_exercises:
                for exercise_data in course_data.exercises_form:
                    self.exercise_form.check_filling(
                        index=course_data.exercises_form.index(exercise_data), form_data=exercise_data
                    )
            else:
                self.exercise_form.check_visible_status_exercises_empty_view(status=True)
