import allure
from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from ui_course.base_class import BaseClass
from ui_course.elements.button.button import Button


class CourseCardMenu(BaseClass):
    def __init__(self, page: Page, step: str):
        super().__init__(page)

        self.substep: str = AllureSubstep.COURSE_CARD_MENU
        self.step = self.generate_step(step=step)

        self.menu_button = Button(
            page=page, locator='course-view-menu-button', name=f'... ({self.substep})', step=self.step
        )
        self.edit_menu_item = Button(
            page=page, locator='course-view-edit-menu-item', name=f'Edit ({self.substep})', step=self.step
        )
        self.delete_menu_item = Button(
            page=page, locator='course-view-delete-menu-item', name=f'Delete ({self.substep})', step=self.step
        )

    def click_edit_button(self, index: int):
        with allure.step(f'{self.step}Нажать кнопки ... -> Edit у курса с индексом {index}'):
            self.menu_button.action.click(nth=index)

            self.edit_menu_item.check.visible_status(status=True)
            self.edit_menu_item.action.click()

    def click_delete_button(self, index: int):
        with allure.step(f'{self.step}Нажать кнопки ... -> Delete у курса с индексом {index}'):
            self.menu_button.action.click(nth=index)

            self.delete_menu_item.check.visible_status(status=True)
            self.delete_menu_item.action.click()
