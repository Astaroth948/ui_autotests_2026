import allure

from ui_course.elements.locator_init import LocatorInit


class BaseElementAction(LocatorInit):
    """
    Класс для базовых действий с элементом страницы.
    """

    def click(self, nth: int = 0, timeout: float | None = None, **kwargs):
        """
        Метод нажатия на элемент.

        :param nth: Индекс элемента.
        :param optional timeout: Таймаут на ожидание элемента.
        :param **kwargs: Данные локатора.
        """

        with allure.step(f'{self.step}Нажать на элемент {self.type_of} "{self.name}" с индексом {nth}'):
            locator = self.get_locator(**kwargs)
            locator.nth(nth).click(timeout=timeout)

    def get_quantity(self, **kwargs) -> int:
        """
        Метод получения количества элементов.

        :param **kwargs: Данные локатора.
        """

        with allure.step(f'{self.step}Получить количество элементов {self.type_of} "{self.name}"'):
            locator = self.get_locator(**kwargs)
            return locator.count()

    def get_visible_status(self, nth: int = 0, **kwargs) -> bool:
        """
        Метод получения статуса отображения элемента.

        :param nth: Индекс элемента.
        :param **kwargs: Данные локатора.
        :return: Статуса отображения элемента в формате `bool`.
        """

        with allure.step(
            f'{self.step}Получить статус отображения элемента {self.type_of} "{self.name}" с индексом {nth}'
        ):
            locator = self.get_locator(**kwargs)
            return locator.nth(nth).is_visible()
