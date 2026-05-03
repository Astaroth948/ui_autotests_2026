import allure
from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from ui_course.components.navigation.header_component import HeaderComponent
from ui_course.components.navigation.sidebar_component import SidebarComponent
from ui_course.pages.base_page import BasePage
from ui_course.pages.courses.course_editor.course_editor_page import CourseEditorPage
from ui_course.pages.courses.courses_list.courses_list_page import CoursesListPage
from ui_course.pages.courses.models import CourseEditorModel


class CoursesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.substep: str = AllureSubstep.COURSES
        self.step = self.generate_step(step=None)

        self.header = HeaderComponent(page=page, step=self.step)
        self.sidebar = SidebarComponent(page=page, step=self.step)
        self.editor = CourseEditorPage(page=page, step=self.step)
        self.list = CoursesListPage(page=page, step=self.step)

    def check_visible_status_base_components(self, status: bool, username: str | None):
        with allure.step(
            '{step}Проверить {status} основных компонентов страниц курсов: Header, Sidebar'.format(
                step=self.step, status='отображение' if status else 'отсутствие'
            )
        ):
            self.header.check_visible_status(status=status, username=username)
            self.sidebar.check_visible_status(status=status)

    def create_course(self, course_data: CourseEditorModel):
        with allure.step(f'{self.step}Создать курс с данными: "{course_data}"'):
            count_courses = self.list.card.get_quantity_courses()

            self.list.toolbar.click_create_course_button()

            self.editor.fill_course(course_data=course_data)
            self.editor.toolbar.click_create_course_button()

            self.list.card.check_quantity_courses(count=count_courses + 1)
            self.list.card.check_course_card(index=count_courses, card_data=course_data.main_form)

    def delete_course(self, index: int):
        with allure.step(f'{self.step}Удалить курс с индексом {index}'):
            count_courses = self.list.card.get_quantity_courses()
            self.list.card.menu.click_delete_button(index=index)
            self.list.modal.click_confirm_button()
            self.list.card.check_quantity_courses(count=count_courses - 1)

    def edit_course(self, index: int, course_data: CourseEditorModel):
        with allure.step(f'{self.step}Изменить данные курса с индексом {index} на "{course_data}"'):
            self.list.card.menu.click_edit_button(index=index)

            self.editor.fill_course(course_data=course_data)
            self.editor.toolbar.click_create_course_button()

            self.list.card.check_course_card(index=index, card_data=course_data.main_form)
