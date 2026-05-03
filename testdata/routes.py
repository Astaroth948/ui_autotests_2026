from enum import StrEnum


class AppRoute(StrEnum):
    """
    Класс для хранения путей URL.
    """

    LOGIN = './#/auth/login'
    REGISTRATION = './#/auth/registration'
    DASHBOARD = './#/dashboard'
    COURSES = './#/courses'
    CREATE_COURSE = './#/courses/create'
    EDIT_COURSE = './#/courses/.*'
