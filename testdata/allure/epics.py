from enum import StrEnum


class AllureEpic(StrEnum):
    """
    Класс для хранения allure epic и parent_suite.
    """

    AUTHENTICATION = 'Аутентификация'
    COURSES = 'Курсы'
    DASHBOARD = 'Дашборды'
