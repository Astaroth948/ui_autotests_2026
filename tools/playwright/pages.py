from typing import Generator

from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright
from pydantic import FilePath

from config import settings
from testdata.directories import TestDataDir
from testdata.files.files import artifact_data
from testdata.settings.browsers import Browsers
from testdata.settings.types import Types
from tools.files import generate_path
from tools.playwright.mocks import mock_static_resources


def save_artifacts(request: SubRequest, page: Page):
    """
    Функция сохраняет тестовые артефакты.

    :param request: Объект `SubRequest`.
    :param page: Объект страницы `Page`.
    """

    artifact_name = request.node.name.split('[')[0] if request.scope == 'function' else artifact_data.storage
    request.node._artifact_name = artifact_name

    if not page.is_closed():
        page.screenshot(
            path=generate_path(directory=TestDataDir.SCREEN_DIR, file_name=artifact_name, extension=Types.PNG)
        )
        page.context.tracing.stop(
            path=generate_path(directory=TestDataDir.TRACING_DIR, file_name=artifact_name, extension=Types.ZIP)
        )
    request.node._video_path = page.video.path()


def init_playwright_page(
    playwright: Playwright, request: SubRequest, browser_type: Browsers, storage_state: FilePath | None = None
) -> Generator[Page, None, None]:
    """
    Функция инициирует объект страницы.

    :param playwright: Объект `Playwright`.
    :param request: Объект `SubRequest`.
    :param browser_type: Тип браузера.
    :param optional storage_state: Ссылка на storage_state.
    """

    browser = playwright[browser_type].launch(headless=settings.browsers_settings.headless)
    context = browser.new_context(
        base_url=str(settings.get_base_url()),
        viewport={'width': settings.browsers_settings.width, 'height': settings.browsers_settings.height},
        storage_state=storage_state,
        record_video_dir=TestDataDir.VIDEOS_DIR,
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    mock_static_resources(page)
    request.node._page = page
    yield page
    save_artifacts(request=request, page=page)
    context.close()
    browser.close()
