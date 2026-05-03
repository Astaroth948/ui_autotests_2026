import allure
from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from ui_course.base_class import BaseClass
from ui_course.elements.input.input import Input
from ui_course.elements.textarea.textarea import Textarea
from ui_course.pages.courses.models import CourseEditorMainFormModel


class CourseEditorMainForm(BaseClass):
    def __init__(self, page: Page, step: str):
        super().__init__(page)

        self.substep: str = AllureSubstep.MAIN_FORM
        self.step = self.generate_step(step=step)

        self.title_input = Input(
            page=page, locator='create-course-form-title-input', name=f'Заголовок ({self.substep})', step=self.step
        )
        self.estimated_time_input = Input(
            page=page,
            locator='create-course-form-estimated-time-input',
            name=f'Estimated time ({self.substep})',
            step=self.step,
        )
        self.description_textarea = Textarea(
            page=page,
            locator='create-course-form-description-input',
            name=f'Description ({self.substep})',
            step=self.step,
        )
        self.max_score_input = Input(
            page=page, locator='create-course-form-max-score-input', name=f'Max score ({self.substep})', step=self.step
        )
        self.min_score_input = Input(
            page=page, locator='create-course-form-min-score-input', name=f'Min score ({self.substep})', step=self.step
        )

    def fill(self, form_data: CourseEditorMainFormModel):
        with allure.step(f'{self.step}Заполнить форму данными: "{form_data}"'):
            self.title_input.action.fill(value=form_data.course_title)
            self.title_input.check.have_value(value=form_data.course_title)

            self.estimated_time_input.action.fill(value=form_data.estimated_time)
            self.estimated_time_input.check.have_value(value=form_data.estimated_time)

            self.description_textarea.action.fill(value=form_data.description)
            self.description_textarea.check.have_value(value=form_data.description)

            self.max_score_input.action.fill(value=form_data.max_score)
            self.max_score_input.check.have_value(value=form_data.max_score)

            self.min_score_input.action.fill(value=form_data.min_score)
            self.min_score_input.check.have_value(value=form_data.min_score)

    def check_filling(self, form_data: CourseEditorMainFormModel):
        with allure.step(f'{self.step}Проверить, что форма заполнена данными: "{form_data}"'):
            self.title_input.check.visible_status(status=True)
            self.title_input.check.have_value(value=form_data.course_title)

            self.estimated_time_input.check.visible_status(status=True)
            self.estimated_time_input.check.have_value(value=form_data.estimated_time)

            self.description_textarea.check.visible_status(status=True)
            self.description_textarea.check.have_value(value=form_data.description)

            self.max_score_input.check.visible_status(status=True)
            self.max_score_input.check.have_value(value=form_data.max_score)

            self.min_score_input.check.visible_status(status=True)
            self.min_score_input.check.have_value(value=form_data.min_score)
