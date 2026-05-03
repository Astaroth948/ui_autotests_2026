from playwright.sync_api import Page

from config import settings


class BaseClass:
    """
    Базовый класс для работы браузером.

    :param page: Объект страницы `Page`.
    """

    def __init__(self, page: Page):
        self.page = page

    def generate_step(self, step: str | None = None) -> str:
        """
        Функция для генерации шага для кастомного отчета allure.

        :param optional step: Описание шага.
        :return: Полный шаг с разделителем " :: " между сущностями.
        """

        if not settings.allure_settings.custom_steps:
            return ''
        if step is not None:
            return f'{step}{self.substep} :: '
        return f'{self.substep} :: '
