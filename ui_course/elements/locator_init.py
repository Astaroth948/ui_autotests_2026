import allure
from playwright.sync_api import Locator, Page

from ui_course.base_class import BaseClass


class LocatorInit(BaseClass):
    """
    Класс для инициализации локатора.

    :param page: Объект страницы `Page`.
    :param locator: Локатор XPATH или data-testid в виде строки.
    :param optional name: Название сущности.
    :param optional child_locator: Дочерний локатор от основного.
    :param optional type_of: Тип сущности.
    :param optional step: Описание шага, предшествующего действию.
    """

    def __init__(
        self, page: Page, locator: str, name: str = None, child_locator: str = None, type_of=None, step: str = ''
    ):
        self.page = page
        self.name = name
        self.locator = locator
        self.child_locator = child_locator
        self.type_of = type_of
        self.step = step

    def generate_locator(self, **kwargs) -> str:
        """
        Функция для генерации локатора.

        :param **kwargs: Данные локатора.
        :return: Полный локатор в виде строки.
        """

        locator_str = self.locator.format(**kwargs)
        if '//' not in locator_str:
            locator_str = f'//*[@data-testid="{locator_str}"]'
        if self.child_locator is not None:
            locator_str += self.child_locator
        return locator_str

    def get_locator(self, **kwargs) -> Locator:
        """
        Функция для получения объекта локатора.

        :param **kwargs: Данные локатора.
        :return: Полный локатор в виде объекта `Locator`.
        """

        locator_str = self.generate_locator(**kwargs)
        with allure.step(f'Получить объект локатора "{locator_str}"'):
            locator = self.page.locator(locator_str)
            return locator
