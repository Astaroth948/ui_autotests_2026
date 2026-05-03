import allure
from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from testdata.text import CourseEditorText
from ui_course.base_class import BaseClass
from ui_course.elements.button.button import Button
from ui_course.elements.text.text import Text


class CourseEditorToolbar(BaseClass):
    def __init__(self, page: Page, step: str):
        super().__init__(page)

        self.substep: str = AllureSubstep.TOOLBAR
        self.step = self.generate_step(step=step)

        self.main_title = Text(
            page=page, locator='create-course-toolbar-title-text', name=f'Заголовок ({self.substep})', step=self.step
        )
        self.create_course_button = Button(
            page=page,
            locator='create-course-toolbar-create-course-button',
            name=f'Create course ({self.substep})',
            step=self.step,
        )
        self.exercises_title = Text(
            page=page,
            locator='create-course-exercises-box-toolbar-title-text',
            name=f'Заголовок формы Exercises ({self.substep})',
            step=self.step,
        )
        self.create_exercise_button = Button(
            page=page,
            locator='create-course-exercises-box-toolbar-create-exercise-button',
            name=f'Create exercise ({self.substep})',
            step=self.step,
        )
        self.delete_exercise_button = Button(
            page=page,
            locator='//button[contains(@data-testid, "-box-toolbar-delete-exercise-button")]',
            name=f'Delete exercise ({self.substep})',
            step=self.step,
        )

    def check_visible_status_toolbar(self, status: bool = True):
        with allure.step(
            '{step}Проверить {status} основных элементов Toolbar: '
            'Заголовок раздела Exercise, Кнопки "Create course" и "Delete exercise"'.format(
                step=self.step, status='отображение' if status else 'отсутствие'
            )
        ):
            self.main_title.check.visible_status(status=status)
            self.exercises_title.check.visible_status(status=status)
            self.create_course_button.check.visible_status(status=status)
            self.create_exercise_button.check.visible_status(status=status)
            if status:
                self.exercises_title.check.have_text(text=CourseEditorText.EXERCISES_TITLE)

    def check_visible_status_create_mode_title(self, status: bool = True):
        with allure.step(
            '{step}Проверить {status} заголовка {title}'.format(
                step=self.step,
                status='отображение' if status else 'отсутствие',
                title=CourseEditorText.CREATE_MODE_TITLE,
            )
        ):
            self.main_title.check.visible_status(status=status)
            if status:
                self.main_title.check.have_text(text=CourseEditorText.CREATE_MODE_TITLE)

    def check_visible_status_edit_mode_title(self, status: bool = True):
        with allure.step(
            '{step}Проверить {status} заголовка {title}'.format(
                step=self.step,
                status='отображение' if status else 'отсутствие',
                title=CourseEditorText.UPDATE_MODE_TITLE,
            )
        ):
            self.main_title.check.visible_status(status=status)
            if status:
                self.main_title.check.have_text(text=CourseEditorText.UPDATE_MODE_TITLE)

    def check_enable_status_create_course_button(self, status: bool = True):
        with allure.step(
            '{step}Проверить состояние {status} кнопки Create course'.format(
                step=self.step, status='enabled' if status else 'disabled'
            )
        ):
            self.create_course_button.check.enable_status(status=status)

    def click_create_course_button(self):
        with allure.step(f'{self.step}Нажать на кнопку "Create course"'):
            self.create_course_button.action.click()

    def click_create_exercise_button(self):
        with allure.step(f'{self.step}Нажать на кнопку "Create exercise"'):
            self.create_exercise_button.action.click()

    def click_delete_exercise_button(self, index: int = 0):
        with allure.step(f'{self.step}Нажать на кнопку "Delete exercise" с индексом {index}'):
            self.delete_exercise_button.action.click(nth=index)

    def get_quantity_delete_exercise_button(self) -> int:
        with allure.step(f'{self.step}Получить количество кнопок "Delete exercise"'):
            return self.delete_exercise_button.action.get_quantity()

    def check_quantity_delete_exercise_buttons(self, count: int):
        with allure.step(f'{self.step}Проверить, что количество кнопок "Delete exercise" равно {count}'):
            self.delete_exercise_button.check.quantity(count=count)

    def set_quantity_exercises(self, count: int):
        with allure.step(f'{self.step}Установить количество форм "Exercise" на {count}'):
            current_count = self.get_quantity_delete_exercise_button()

            if current_count < count:
                for _ in range(current_count, count):
                    self.click_create_exercise_button()

            if current_count > count:
                for index in range(current_count, count, -1):
                    self.click_delete_exercise_button(index=index - 1)

            self.check_quantity_delete_exercise_buttons(count=count)
