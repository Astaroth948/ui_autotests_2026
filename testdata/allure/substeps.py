from enum import StrEnum


class AllureSubstep(StrEnum):
    """
    Класс для хранения подшагов для генерации кастомного отчета.
    """

    AUTHENTICATION = 'Аутентификация'
    LOGIN_FORM = 'Форма авторизации'
    REGISTRATION_FORM = 'Форма регистрации'
    COURSES = 'Курсы'
    CREATE_COURSE = 'Редактор курса'
    MAIN_FORM = 'Главная форма'
    EXERCISE_FORM = 'Форма раздела Exercise'
    COURSES_LIST = 'Список курсов'
    COURSE_CARD_MENU = 'Меню карточки курса'
    COURSE_CARD = 'Карточка курса'
    DASHBOARD = 'Дашборд'
    ALERTS = 'Алерты'
    CHARTS = 'Графики'
    HEADER = 'Header'
    TOOLBAR = 'Toolbar'
    SIDEBAR = 'Sidebar'
    EMPTY_VIEW = 'Empty View'
    IMAGE_UPLOAD_WIDGET = 'Image Upload Widget'
    MODAL = 'Модальное окно'
