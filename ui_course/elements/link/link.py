from playwright.sync_api import Page

from ui_course.elements.base_element.action import BaseElementAction
from ui_course.elements.base_element.base_element import BaseElement
from ui_course.elements.base_element.check import BaseElementCheck


class Link(BaseElement):
    """
    Класс для действий и проверок элемента link.
    """

    def __init__(self, page: Page, locator: str, name: str = None, child_locator: str = None, step: str = ''):
        super().__init__(page, locator, name, child_locator, step)

        self.type_of: str = 'link'
        self.action = BaseElementAction(
            page=page, locator=locator, name=name, child_locator=child_locator, type_of=self.type_of, step=step
        )
        self.check = BaseElementCheck(
            page=page, locator=locator, name=name, child_locator=child_locator, type_of=self.type_of, step=step
        )
