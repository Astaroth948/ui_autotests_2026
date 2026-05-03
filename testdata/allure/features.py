from enum import StrEnum


class AllureFeature(StrEnum):
    """
    Класс для хранения allure feature и suite.
    """

    FUNCTIONAL = 'Общий функционал'
    NAVIGATION = 'Навигация'
    VIEW = 'Внешний вид'

    FAILED = 'Failed тесты (для демонстрации отчета)'
