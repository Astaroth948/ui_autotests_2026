import allure

from ui_course.elements.base_element.action import BaseElementAction


class InputAction(BaseElementAction):
    """
    Класс для действий с элементом input.
    """

    def fill(self, value: str, nth: int = 0, timeout: float | None = None, **kwargs):
        """
        Метод ввода текста.

        :param value: Значение ввода.
        :param nth: Индекс элемента.
        :param optional timeout: Таймаут на ожидание элемента.
        :param **kwargs: Данные локатора.
        """

        with allure.step(f'{self.step}Ввести в {self.type_of} "{self.name}" с индексом {nth} текст "{value}"'):
            locator = self.get_locator(**kwargs)
            locator.nth(nth).fill(value, timeout=timeout)
