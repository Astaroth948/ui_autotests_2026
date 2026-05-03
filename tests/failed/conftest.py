from typing import Generator

import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright

from config import settings
from testdata.courses import PRECONDITION_COURSES_LIST
from testdata.files.files import TestDataFiles
from testdata.routes import AppRoute
from testdata.users import UsersData
from tools.playwright.pages import init_playwright_page
from ui_course.pages.authentication.auth_page import AuthPage
from ui_course.pages.courses.courses_page import CoursesPage


@pytest.fixture
def failed_fixture_setup(courses_page_with_courses: CoursesPage):
    courses_page_with_courses.visit(url=AppRoute.COURSES)
    courses_page_with_courses.list.check_courses_cards(cards_list=PRECONDITION_COURSES_LIST)
    assert 0
    courses_page_with_courses.list.card.menu.click_delete_button(index=0)
    courses_page_with_courses.list.check_visible_status_delete_course_modal(status=True)
    courses_page_with_courses.list.modal.click_confirm_button()


@pytest.fixture
def failed_fixture_teardown(courses_page_with_courses: CoursesPage):
    yield
    courses_page_with_courses.visit(url=AppRoute.COURSES)
    courses_page_with_courses.list.card.menu.click_edit_button(index=0)
    courses_page_with_courses.check_visible_status_base_components(
        status=True, username=UsersData.DEFAULT_USER.username
    )
    courses_page_with_courses.editor.toolbar.check_visible_status_toolbar(status=True)
    courses_page_with_courses.editor.toolbar.check_visible_status_edit_mode_title(status=True)
    assert 0
    courses_page_with_courses.editor.toolbar.check_enable_status_create_course_button(status=True)


@pytest.fixture(scope='session', params=settings.browsers_settings.browsers)
def page_session_2(request: SubRequest, playwright: Playwright) -> Generator[Page, None, None]:
    yield from init_playwright_page(playwright=playwright, request=request, browser_type=request.param)


@pytest.fixture(scope='session')
def init_browser_state_failed_session(page_session_2: Page):
    auth_page = AuthPage(page=page_session_2)
    auth_page.visit(url=AppRoute.REGISTRATION)
    auth_page.reg_form.fill(user_data=UsersData.DEFAULT_USER)
    assert 0
    auth_page.check_current_url(expected_url=AppRoute.DASHBOARD)

    page_session_2.context.close()
    page_session_2.context.browser.close()


@pytest.fixture(params=settings.browsers_settings.browsers)
def page_failed(
    request: SubRequest, init_browser_state_failed_session, playwright: Playwright
) -> Generator[Page, None, None]:
    yield from init_playwright_page(
        playwright=playwright,
        request=request,
        browser_type=request.param,
        storage_state=TestDataFiles.BROWSER_STATE_IGNORE_LOGIN,
    )


@pytest.fixture
def courses_page_failed(page_failed: Page) -> CoursesPage:
    return CoursesPage(page=page_failed)


@pytest.fixture(scope='class', params=settings.browsers_settings.browsers)
def page_with_courses_class(
    request: SubRequest, init_browser_state, playwright: Playwright
) -> Generator[Page, None, None]:
    yield from init_playwright_page(
        playwright=playwright,
        request=request,
        browser_type=request.param,
        storage_state=TestDataFiles.BROWSER_STATE_WITH_COURSES,
    )


@pytest.fixture
def courses_page_from_class(page_with_courses_class: Page) -> CoursesPage:
    return CoursesPage(page=page_with_courses_class)


@pytest.fixture(scope='class')
def failed_fixture_setup_class(page_with_courses_class):
    courses_page = CoursesPage(page=page_with_courses_class)
    courses_page.visit(url=AppRoute.DASHBOARD)
    courses_page.check_current_url(expected_url=AppRoute.DASHBOARD)
    assert 0

    yield
    courses_page.visit(url=AppRoute.CREATE_COURSE)
    courses_page.check_current_url(expected_url=AppRoute.CREATE_COURSE)


@pytest.fixture(scope='module', params=settings.browsers_settings.browsers)
def page_with_courses_module(
    request: SubRequest, init_browser_state, playwright: Playwright
) -> Generator[Page, None, None]:
    yield from init_playwright_page(
        playwright=playwright,
        request=request,
        browser_type=request.param,
        storage_state=TestDataFiles.BROWSER_STATE_WITH_COURSES,
    )


@pytest.fixture
def courses_page_from_module(page_with_courses_module: Page) -> CoursesPage:
    return CoursesPage(page=page_with_courses_module)


@pytest.fixture(scope='module')
def failed_fixture_setup_module(page_with_courses_module):
    courses_page = CoursesPage(page=page_with_courses_module)
    courses_page.visit(url=AppRoute.COURSES)
    courses_page.check_current_url(expected_url=AppRoute.COURSES)

    courses_page.list.card.menu.click_edit_button(index=2)
    courses_page.check_visible_status_base_components(status=True, username=UsersData.DEFAULT_USER.username)

    assert 0

    yield
    courses_page.visit(url=AppRoute.CREATE_COURSE)
    courses_page.check_current_url(expected_url=AppRoute.CREATE_COURSE)
