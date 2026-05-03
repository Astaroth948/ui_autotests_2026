import allure
from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from testdata.text import CourseCardFieldsText
from ui_course.base_class import BaseClass
from ui_course.components.views.empty_view_component import EmptyViewComponent
from ui_course.elements.image.image import Image
from ui_course.elements.text.text import Text
from ui_course.pages.courses.courses_list.components.card_menu import CourseCardMenu
from ui_course.pages.courses.models import CourseCardModel


class CourseCard(BaseClass):
    def __init__(self, page: Page, step: str):
        super().__init__(page)

        self.substep: str = AllureSubstep.COURSE_CARD
        self.step = self.generate_step(step=step)

        self.empty_list = EmptyViewComponent(page=page, identifier='courses-list', step=self.step)
        self.menu = CourseCardMenu(page=page, step=self.step)

        self.title = Text(
            page=page, locator='course-widget-title-text', name=f'Заголовок ({self.substep})', step=self.step
        )
        self.image = Image(page=page, locator='course-preview-image', name=f'Превью ({self.substep})', step=self.step)
        self.max_score_text = Text(
            page=page, locator='course-max-score-info-row-view-text', name=f'Max score ({self.substep})', step=self.step
        )
        self.min_score_text = Text(
            page=page, locator='course-min-score-info-row-view-text', name=f'Min score ({self.substep})', step=self.step
        )
        self.estimated_time_text = Text(
            page=page,
            locator='course-estimated-time-info-row-view-text',
            name=f'Estimated time ({self.substep})',
            step=self.step,
        )

    def check_course_card(self, index: int, card_data: CourseCardModel):
        with allure.step(f'{self.step}Проверить у карточки с индексом {index} отображение данных: "{card_data}"'):
            self.image.check.visible_status(status=True, nth=index)

            self.title.check.visible_status(status=True, nth=index)
            self.title.check.have_text(text=card_data.course_title, nth=index)

            self.max_score_text.check.visible_status(status=True, nth=index)
            self.max_score_text.check.have_text(
                text=CourseCardFieldsText.MAX_SCORE.format(max_score=card_data.max_score), nth=index
            )

            self.min_score_text.check.visible_status(status=True, nth=index)
            self.min_score_text.check.have_text(
                text=CourseCardFieldsText.MIN_SCORE.format(min_score=card_data.min_score), nth=index
            )

            self.estimated_time_text.check.visible_status(status=True, nth=index)
            self.estimated_time_text.check.have_text(
                text=CourseCardFieldsText.ESTIMATED_TIME.format(estimated_time=card_data.estimated_time), nth=index
            )

    def get_quantity_courses(self) -> int:
        with allure.step(f'{self.step}Получить количество карточек'):
            return self.image.action.get_quantity()

    def check_quantity_courses(self, count: int):
        with allure.step(f'{self.step}Проверить, что количество карточек равно {count}'):
            self.image.check.quantity(count=count)
