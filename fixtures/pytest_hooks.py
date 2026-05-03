import pytest
from _pytest.fixtures import FixtureDef, SubRequest
from pluggy._result import Result
from pytest import Item, TestReport

from config import settings
from testdata.directories import TestDataDir
from testdata.files.files import artifact_data
from tools.allure.attach import attach_screen_file, attach_trace_file, attach_video_file, make_screen_and_attach
from tools.allure.report import attach_attachments_fail_fixtures_tests, format_tags_report, generate_custom_report
from tools.files import clear_directories


def pytest_configure(config):
    """
    Pytest hook для автоматической очистки allure отчетов
    перед запуском автотестов в зависимости от настроек.
    """

    if settings.allure_settings.clear_reports_at_start:
        clear_directories([TestDataDir.ALLURE_RESULTS_DIR])


@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef: FixtureDef, request: SubRequest):
    """
    Pytest hook для обнаружения падения фикстур со scope
    [class, module, session] на предусловиях
    """

    item = request.node
    artifact_data(name=fixturedef.argname)

    outcome: Result = yield
    if outcome.excinfo and fixturedef.scope in ['session', 'class', 'module']:
        item._setup_fail = True
        item._artifact_name = artifact_data.storage
        item._attach_fixture = fixturedef.argnames[0]


@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_post_finalizer(fixturedef: FixtureDef, request: SubRequest):
    """
    Pytest hook для обнаружения падения фикстур со scope
    [class, module, session] на постусловиях
    """

    item = request.node

    page = getattr(item, '_page', None)
    video_path = getattr(item, '_video_path', None)

    if not getattr(item, '_setup_screen_attached', False):
        if getattr(item, '_setup_fail', False):
            make_screen_and_attach(
                page=page, alias=f"fixture_{request.scope}_setup ({getattr(item, '_artifact_name', '')})"
            )
            item._setup_screen_attached = True

    outcome: Result = yield
    # TODO Не работает
    if outcome.excinfo and fixturedef.scope in ['session', 'class', 'module']:
        item._teardown_fail = True

    if fixturedef.argname == getattr(item, '_attach_fixture', None):
        if not getattr(item, '_fixture_files_attached', False):
            artifact_name = getattr(item, '_artifact_name', '')
            if getattr(item, '_teardown_fail', False):
                attach_screen_file(
                    artifact_name=artifact_name, alias=f'fixture_{request.scope}_teardown ({artifact_name})'
                )
            if getattr(item, '_setup_fail', False) or getattr(item, '_teardown_fail', False):
                attach_trace_file(artifact_name=artifact_name, alias=f'fixture_{request.scope} ({artifact_name})')
                attach_video_file(video_path=video_path, alias=f'fixture_{request.scope} ({artifact_name})')
            item._fixture_files_attached = True


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item):
    """
    Pytest hook для обнаружения падения тестов и фикстур со scope function
    """

    outcome: Result = yield
    test_result: TestReport = outcome.get_result()
    artifact_name = getattr(item, '_artifact_name', item.name.split('[')[0])

    if test_result.when in ['setup', 'call']:
        if test_result.failed or (test_result.skipped and hasattr(test_result, 'wasxfail')):
            item._test_failed = True
            page = getattr(item, '_page', None)
            if page is not None:
                make_screen_and_attach(page=page, alias=f'test_{test_result.when} ({artifact_name})')

    if test_result.when in ['teardown']:
        if test_result.failed or (test_result.skipped and hasattr(test_result, 'wasxfail')):
            item._test_failed = True
            attach_screen_file(artifact_name=artifact_name, alias=f'test_{test_result.when} ({artifact_name})')
        if getattr(item, '_test_failed', False):
            video_path = getattr(item, '_video_path', None)
            attach_trace_file(artifact_name=artifact_name, alias=f'test ({artifact_name})')
            attach_video_file(video_path=video_path, alias=f'test ({artifact_name})')


def pytest_terminal_summary(terminalreporter, exitstatus):
    """
    Pytest hook для завершения тестового прогона.
    Очистка тестовых артефактов.
    Прикрепление недостающих аттачей при падении фикстур со scope [class, module, session]
    Генерация кастомного отчета allure.
    Преобразование Pytest тегов в формат UPPER_SNAKE_CASE в allure отчете.
    """

    clear_directories([TestDataDir.TRACING_DIR, TestDataDir.SCREEN_DIR, TestDataDir.VIDEOS_DIR])
    attach_attachments_fail_fixtures_tests(directory=TestDataDir.ALLURE_RESULTS_DIR)
    generate_custom_report(directory=TestDataDir.ALLURE_RESULTS_DIR)
    format_tags_report(directory=TestDataDir.ALLURE_RESULTS_DIR)
