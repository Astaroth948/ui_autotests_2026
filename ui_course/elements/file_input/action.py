import allure
from pydantic import FilePath

from ui_course.elements.base_element.action import BaseElementAction


class FileInputAction(BaseElementAction):
    """
    Класс для действий с элементом file input.
    """

    def set_input_files(self, file: FilePath, nth: int = 0, timeout: float | None = None, **kwargs):
        """
        Метод загрузки файла.

        :param file: Ссылка на файл в формате `FilePath`.
        :param nth: Индекс элемента.
        :param optional timeout: Таймаут на ожидание элемента.
        :param **kwargs: Данные локатора.
        """

        with allure.step(f'{self.step}Загрузить файл "{file}" в элемент {self.type_of} "{self.name}" с индексом {nth}'):
            locator = self.get_locator(**kwargs)
            locator.nth(nth).set_input_files(file, timeout=timeout)
