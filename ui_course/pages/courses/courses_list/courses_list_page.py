from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from testdata.text import EmptyViewText, ModalText
from ui_course.components.modal.modal_component import ModalComponent
from ui_course.pages.base_page import BasePage
from ui_course.pages.courses.courses_list.components.card import CourseCard
from ui_course.pages.courses.courses_list.components.toolbar import CoursesListToolbar
from ui_course.pages.courses.models import CourseCardModel


class CoursesListPage(BasePage):
    def __init__(self, page: Page, step: str):
        super().__init__(page)

        self.substep: str = AllureSubstep.COURSES_LIST
        self.step = self.generate_step(step=step)

        self.card = CourseCard(page=page, step=self.step)
        self.modal = ModalComponent(page=page, step=self.step)
        self.toolbar = CoursesListToolbar(page=page, step=self.step)

    def check_visible_status_empty_view(self, status: bool = True):
        self.card.empty_list.check_visible_status(
            status=status, title=EmptyViewText.NO_COURSES_TITLE, description=EmptyViewText.NO_COURSES_DESCRIPTION
        )

    def check_visible_status_delete_course_modal(self, status: bool = True):
        self.modal.check_visible_status(
            status=status, title=ModalText.DELETE_COURSE_TITLE, message=ModalText.DELETE_COURSE_MESSAGE
        )

    def check_courses_cards(self, cards_list: list[CourseCardModel]):
        count_cards = len(cards_list)
        if count_cards:
            self.card.check_quantity_courses(count=count_cards)
            for card_data in cards_list:
                self.card.check_course_card(index=cards_list.index(card_data), card_data=card_data)
        else:
            self.check_visible_status_empty_view(status=True)
