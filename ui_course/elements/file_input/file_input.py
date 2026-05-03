from playwright.sync_api import Page

from ui_course.elements.base_element.check import BaseElementCheck
from ui_course.elements.file_input.action import FileInputAction
from ui_course.elements.locator_init import LocatorInit


class FileInput(LocatorInit):
    """
    Класс для действий и проверок элемента file input.
    """

    def __init__(self, page: Page, locator: str, name: str = None, child_locator: str = None, step: str = ''):
        super().__init__(page, locator, name, child_locator, step)

        self.type_of: str = 'file input'
        self.action = FileInputAction(
            page=page, locator=locator, name=name, child_locator=child_locator, type_of=self.type_of, step=step
        )
        self.check = BaseElementCheck(
            page=page, locator=locator, name=name, child_locator=child_locator, type_of=self.type_of, step=step
        )
