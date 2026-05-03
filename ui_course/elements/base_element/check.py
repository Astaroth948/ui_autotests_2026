import allure
from playwright.sync_api import expect

from ui_course.elements.locator_init import LocatorInit


class BaseElementCheck(LocatorInit):
    """
    Класс для базовых проверок элемента страницы.
    """

    def visible_status(self, status: bool = True, nth: int = 0, timeout: float | None = None, **kwargs):
        """
        Метод проверки отображения элемента.

        :param status: Ожидаемый статус отображения элемента.
        :param nth: Индекс элемента.
        :param optional timeout: Таймаут на ожидание элемента.
        :param **kwargs: Данные локатора.
        """

        with allure.step(
            '{step}Проверить {status} элемента {type_of} "{name}" с индексом {nth}'.format(
                step=self.step,
                status='отображение' if status else 'отсутствие',
                type_of=self.type_of,
                name=self.name,
                nth=nth,
            )
        ):
            locator = self.get_locator(**kwargs)
            if status:
                expect(locator.nth(nth)).to_be_visible(timeout=timeout)
            else:
                expect(locator.nth(nth)).to_be_hidden(timeout=timeout)

    def have_text(self, text: str, nth: int = 0, timeout: float | None = None, **kwargs):
        """
        Метод проверки текста элемента.

        :param text: Ожидаемый текст элемента.
        :param nth: Индекс элемента.
        :param optional timeout: Таймаут на ожидание элемента.
        :param **kwargs: Данные локатора.
        """

        with allure.step(
            f'{self.step}Проверить, что текст элемента {self.type_of} "{self.name}" с индексом {nth} равен "{text}"'
        ):
            locator = self.get_locator(**kwargs)
            expect(locator.nth(nth)).to_have_text(text, timeout=timeout)

    def enable_status(self, status: bool = True, nth: int = 0, timeout: float | None = None, **kwargs):
        """
        Метод проверки статуса доступности элемента через атрибуты enabled и disabled.

        ::param status: Ожидаемый статус доступности элемента.
        :param nth: Индекс элемента.
        :param optional timeout: Таймаут на ожидание элемента.
        :param **kwargs: Данные локатора.
        """

        with allure.step(
            '{step}Проверить, что элемент {type_of} "{name}" с индексом {nth} в состоянии {status}'.format(
                step=self.step,
                type_of=self.type_of,
                name=self.name,
                nth=nth,
                status='enabled' if status else 'disabled',
            )
        ):
            locator = self.get_locator(**kwargs)
            if status:
                expect(locator.nth(nth)).to_be_enabled(timeout=timeout)
            else:
                expect(locator.nth(nth)).to_be_disabled(timeout=timeout)

    def quantity(self, count: int, timeout: float | None = None, **kwargs):
        """
        Метод проверки количества элементов.

        ::param count: Ожидаемое количество элементов.
        :param optional timeout: Таймаут на ожидание элемента.
        :param **kwargs: Данные локатора.
        """

        with allure.step(
            f'{self.step}Проверить, что количество элементов {self.type_of} "{self.name}" равно "{count}"'
        ):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_count(count, timeout=timeout)
