from typing import Generator

import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright

from config import settings
from testdata.courses import CourseEditorData
from testdata.files.files import TestDataFiles
from testdata.routes import AppRoute
from testdata.users import UsersData
from tools.playwright.pages import init_playwright_page
from ui_course.pages.authentication.auth_page import AuthPage
from ui_course.pages.courses.courses_page import CoursesPage


@pytest.fixture(params=settings.browsers_settings.browsers)
def page(request: SubRequest, playwright: Playwright) -> Generator[Page, None, None]:
    """
    Фикстура для инициализации объекта Playwright Page.

    :scope: function.
    """

    yield from init_playwright_page(playwright=playwright, request=request, browser_type=request.param)


@pytest.fixture(scope='session', params=settings.browsers_settings.browsers)
def page_session(request: SubRequest, playwright: Playwright) -> Generator[Page, None, None]:
    """
    Фикстура для инициализации объекта Playwright Page.

    :scope: session.
    """

    yield from init_playwright_page(playwright=playwright, request=request, browser_type=request.param)


@pytest.fixture(scope='session')
def init_browser_state(page_session: Page):
    """
    Фикстура для подготовки тестового окружения через storage_state.

    :scope: session.
    """

    browser_state_ignore_login = TestDataFiles.BROWSER_STATE_IGNORE_LOGIN
    browser_state_with_courses = TestDataFiles.BROWSER_STATE_WITH_COURSES

    auth_page = AuthPage(page=page_session)
    auth_page.visit(url=AppRoute.REGISTRATION)
    auth_page.registration_user(user_data=UsersData.DEFAULT_USER)
    auth_page.check_current_url(expected_url=AppRoute.DASHBOARD)

    auth_page.page.context.storage_state(path=browser_state_ignore_login)

    courses_page = CoursesPage(page=page_session)
    courses_page.visit(url=AppRoute.COURSES)
    for course_data in [
        CourseEditorData.COURSE_PYTHON,
        CourseEditorData.COURSE_PLAYWRIGHT,
        CourseEditorData.COURSE_SELENIUM,
    ]:
        courses_page.create_course(course_data=course_data)

    courses_page.page.context.storage_state(path=browser_state_with_courses)

    page_session.context.close()
    page_session.context.browser.close()


@pytest.fixture(params=settings.browsers_settings.browsers)
def page_ignore_login(request: SubRequest, init_browser_state, playwright: Playwright) -> Generator[Page, None, None]:
    """
    Фикстура для инициализации объекта Playwright Page с игнорированием авторизациии
    через готовый storage_state.

    :scope: function.
    """

    yield from init_playwright_page(
        playwright=playwright,
        request=request,
        browser_type=request.param,
        storage_state=TestDataFiles.BROWSER_STATE_IGNORE_LOGIN,
    )


@pytest.fixture(params=settings.browsers_settings.browsers)
def page_with_courses(request: SubRequest, init_browser_state, playwright: Playwright) -> Generator[Page, None, None]:
    """
    Фикстура для инициализации объекта Playwright Page с игнорированием авторизациии
    и заготовленными тестовыми данными через storage_state.

    :scope: function.
    """

    yield from init_playwright_page(
        playwright=playwright,
        request=request,
        browser_type=request.param,
        storage_state=TestDataFiles.BROWSER_STATE_WITH_COURSES,
    )
