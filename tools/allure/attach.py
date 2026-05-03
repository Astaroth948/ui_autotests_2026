import os

import allure
from playwright.sync_api import Page

from config import settings
from testdata.directories import TestDataDir
from testdata.settings.types import Types
from tools.files import generate_path


def attach_screen_file(artifact_name: str, alias: str):
    """
    Функция прикрепляет сохраненный скриншот к allure отчету.

    :param artifact_name: Имя скриншота.
    :param alias: Имя скриншота, которое будет отборажаться в отчете.
    """

    screen_path = generate_path(directory=TestDataDir.SCREEN_DIR, file_name=artifact_name, extension=Types.PNG)
    if settings.allure_settings.screens and os.path.exists(screen_path):
        allure.attach.file(screen_path, name=f'screen_{alias}', attachment_type=allure.attachment_type.PNG)


def make_screen_and_attach(page: Page, alias: str):
    """
    Функция делает скриншот и прикрепляет его к allure отчету.

    :param page: Объект страницы, для который необходимо сделать скриншот.
    :param alias: Имя скриншота, которое будет отборажаться в отчете.
    """

    if settings.allure_settings.screens:
        allure.attach(page.screenshot(), name=f'screen_{alias}', attachment_type=allure.attachment_type.PNG)


def attach_video_file(video_path: str | None, alias: str):
    """
    Функция прикрепляет сохраненное видео к allure отчету.

    :param video_path: Полный путь к видео.
    :param alias: Имя скриншота, которое будет отборажаться в отчете.
    """

    if settings.allure_settings.videos and video_path is not None:
        if os.path.exists(video_path):
            allure.attach.file(video_path, name=f'video_{alias}', attachment_type=allure.attachment_type.WEBM)


def attach_trace_file(artifact_name: str, alias: str):
    """
    Функция прикрепляет сохраненный trace к allure отчету.

    :param artifact_name: Имя trace.
    :param alias: Имя trace, которое будет отборажаться в отчете.
    """

    trace_path = generate_path(directory=TestDataDir.TRACING_DIR, file_name=artifact_name, extension=Types.ZIP)
    if settings.allure_settings.tracing and os.path.exists(trace_path):
        allure.attach.file(trace_path, name=f'trace_{alias}', extension=Types.ZIP)
