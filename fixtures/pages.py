import pytest
from playwright.sync_api import Page

from ui_course.pages.authentication.auth_page import AuthPage
from ui_course.pages.courses.courses_page import CoursesPage
from ui_course.pages.dashboard.dashboard_page import DashboardPage


@pytest.fixture
def auth_page(page: Page) -> AuthPage:
    """
    Фикстура для инициализации объекта класса страницы аутентификации.

    :scope: function.
    :return: Объект класса страницы `AuthPage`.
    """

    return AuthPage(page=page)


@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    """
    Фикстура для инициализации объекта класса страницы Dashboard.

    :scope: function.
    :return: Объект класса страницы `DashboardPage`.
    """

    return DashboardPage(page=page)


@pytest.fixture
def dashboard_page_ignore_login(page_ignore_login: Page) -> DashboardPage:
    """
    Фикстура для инициализации объекта класса страницы Dashboard
    с пропущенной авторизацией.

    :scope: function.
    :return: Объект класса страницы `DashboardPage`.
    """

    return DashboardPage(page=page_ignore_login)


@pytest.fixture
def courses_page_ignore_login(page_ignore_login: Page) -> CoursesPage:
    """
    Фикстура для инициализации объекта класса страницы курсов
    с пропущенной авторизацией.

    :scope: function.
    :return: Объект класса страницы `CoursesPage`.
    """

    return CoursesPage(page=page_ignore_login)


@pytest.fixture
def courses_page_with_courses(page_with_courses: Page) -> CoursesPage:
    """
    Фикстура для инициализации объекта класса страницы курсов
    с пропущенной авторизацией и заготовленными тестовыми данными.

    :scope: function.
    :return: Объект класса страницы `CoursesPage`.
    """

    return CoursesPage(page=page_with_courses)
