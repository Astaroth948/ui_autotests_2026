from playwright.sync_api import Page

from ui_course.elements.input.action import InputAction
from ui_course.elements.input.check import InputCheck
from ui_course.elements.locator_init import LocatorInit


class Input(LocatorInit):
    """
    Класс для действий и проверок элемента input.
    """

    def __init__(self, page: Page, locator: str, name: str = None, child_locator: str = '//input', step: str = ''):
        super().__init__(page, locator, name, child_locator, step)

        self.type_of: str = 'input'
        self.action = InputAction(
            page=page, locator=locator, name=name, child_locator=child_locator, type_of=self.type_of, step=step
        )
        self.check = InputCheck(
            page=page, locator=locator, name=name, child_locator=child_locator, type_of=self.type_of, step=step
        )
