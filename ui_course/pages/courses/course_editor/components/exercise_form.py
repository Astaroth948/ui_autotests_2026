import allure
from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from testdata.text import CourseEditorText, EmptyViewText
from ui_course.base_class import BaseClass
from ui_course.components.views.empty_view_component import EmptyViewComponent
from ui_course.elements.input.input import Input
from ui_course.elements.text.text import Text
from ui_course.pages.courses.models import CourseEditorExercisesFormModel


class CourseEditorExerciseForm(BaseClass):
    def __init__(self, page: Page, step: str):
        super().__init__(page)

        self.substep: str = AllureSubstep.EXERCISE_FORM
        self.step = self.generate_step(step=step)

        self.subtitle = Text(
            page=page,
            locator='create-course-exercise-{index}-box-toolbar-subtitle-text',
            name=f'Подзаголовок группы Exercise ({self.substep})',
            step=self.step,
        )
        self.title_input = Input(
            page=page,
            locator='create-course-exercise-form-title-{index}-input',
            name=f'Title ({self.substep})',
            step=self.step,
        )
        self.description_input = Input(
            page=page,
            locator='create-course-exercise-form-description-{index}-input',
            name=f'Description ({self.substep})',
            step=self.step,
        )

        self.empty_view = EmptyViewComponent(page=page, identifier='create-course-exercises', step=self.step)

    def fill(self, index: int, form_data: CourseEditorExercisesFormModel):
        with allure.step(f'{self.step}Заполнить форму с индексом {index} данными: "{form_data}"'):
            self.title_input.action.fill(value=form_data.exercise_title, index=index)
            self.title_input.check.have_value(value=form_data.exercise_title, index=index)

            self.description_input.action.fill(value=form_data.description, index=index)
            self.description_input.check.have_value(value=form_data.description, index=index)

    def check_filling(self, index: int, form_data: CourseEditorExercisesFormModel):
        with allure.step(f'{self.step}Проверить, что форма с индексом {index} заполнена данными: "{form_data}"'):
            self.subtitle.check.visible_status(status=True, index=index)
            self.subtitle.check.have_text(text=CourseEditorText.EXERCISE_SUBTITLE.format(index=index + 1), index=index)

            self.title_input.check.visible_status(status=True, index=index)
            self.title_input.check.have_value(value=form_data.exercise_title, index=index)

            self.description_input.check.visible_status(status=True, index=index)
            self.description_input.check.have_value(value=form_data.description, index=index)

    def check_visible_status_exercises_empty_view(self, status: bool = True):
        self.empty_view.check_visible_status(
            status=status, title=EmptyViewText.NO_EXERCIES_TITLE, description=EmptyViewText.NO_EXERCIES_DESCRIPTION
        )
