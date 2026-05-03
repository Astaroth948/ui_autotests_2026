from enum import StrEnum


class AllureStory(StrEnum):
    """
    Класс для хранения allure story и sub_suite.
    """

    COURSE_EDITOR = 'Страница редактора курсов'
    COURSES_LIST = 'Страница списка курсоа'
    CREATE = 'Проверки создания'
    DASHBOARD = 'Страница Dashboard'
    DELETE = 'Проверки удаления'
    EDIT = 'Проверки редактирования'
    LINKED_PAGES = 'Связанные страницы'
    LOGIN = 'Страница авторизации'
    REGISTRATION = 'Страница регистрации'
    STORY = 'Проверки User Story'
    VIEW = 'Проверки внешнего вида'

    FAILED = 'Failed тесты'
    X_FAILED = 'X-Failed тесты'
    CUSTOM_REPORT = 'Failed тесты с заведенными багами'
