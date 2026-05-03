import allure
from playwright.sync_api import expect

from ui_course.elements.base_element.check import BaseElementCheck


class InputCheck(BaseElementCheck):
    """
    Класс для проверок элемента input.
    """

    def have_value(self, value: str, nth: int = 0, timeout: float | None = None, **kwargs):
        """
        Метод проверки текста.

        :param value: Значение текста.
        :param nth: Индекс элемента.
        :param optional timeout: Таймаут на ожидание элемента.
        :param **kwargs: Данные локатора.
        """

        with allure.step(
            f'{self.step}Проверить, что значение элемента {self.type_of} "{self.name}" с индексом {nth} равно "{value}"'
        ):
            locator = self.get_locator(**kwargs)
            expect(locator.nth(nth)).to_have_value(value, timeout=timeout)
