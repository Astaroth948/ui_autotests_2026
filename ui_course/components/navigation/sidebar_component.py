import allure
from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from testdata.text import SidebarText
from ui_course.base_class import BaseClass
from ui_course.components.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseClass):
    def __init__(self, page: Page, step: str):
        super().__init__(page)

        self.substep: str = AllureSubstep.SIDEBAR
        self.step = self.generate_step(step=step)

        self.logout_list_item = SidebarListItemComponent(page=page, identifier='logout', step=self.step)
        self.courses_list_item = SidebarListItemComponent(page=page, identifier='courses', step=self.step)
        self.dashboard_list_item = SidebarListItemComponent(page=page, identifier='dashboard', step=self.step)

    def check_visible_status(self, status: bool = True):
        with allure.step(
            '{step}Проверить {status} кнопок навигации'.format(
                step=self.step, status='отображение' if status else 'отсутствие'
            )
        ):
            self.logout_list_item.check_visible_status(status=status, title=SidebarText.LOGOUT)
            self.courses_list_item.check_visible_status(status=status, title=SidebarText.COURSES)
            self.dashboard_list_item.check_visible_status(status=status, title=SidebarText.DASHBOARD)

    def click_logout_button(self):
        with allure.step(f'{self.step}Нажать Logout'):
            self.logout_list_item.button.action.click()

    def click_courses_button(self):
        with allure.step(f'{self.step}Нажать Courses'):
            self.courses_list_item.button.action.click()

    def click_dashboard_button(self):
        with allure.step(f'{self.step}Нажать Dashboard'):
            self.dashboard_list_item.button.action.click()
