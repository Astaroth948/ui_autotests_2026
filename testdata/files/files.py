from pydantic import FilePath

from testdata.directories import TestDataDir
from testdata.settings.types import Types
from tools.files import generate_path


def artifact_data(name: str | None = None) -> str:
    """
    Функция для хранения данных артефактов при падении теста.

    :param name: Название артефакта.
    :return: Хранимое название артефакта.
    """

    if not hasattr(artifact_data, 'storage'):
        artifact_data.storage = ''
    else:
        artifact_data.storage = name
    return artifact_data.storage


class TestDataFiles:
    """
    Класс для хранения путей файлов.
    """

    BROWSER_STATE_IGNORE_LOGIN: FilePath = generate_path(
        directory=TestDataDir.BROWSER_STATE_DIR, file_name='browser_state_ignore_login', extension=Types.JSON
    )
    BROWSER_STATE_WITH_COURSES: FilePath = generate_path(
        directory=TestDataDir.BROWSER_STATE_DIR, file_name='browser_state_with_courses', extension=Types.JSON
    )
    IMAGE_PYTHON: FilePath = generate_path(
        directory=TestDataDir.IMAGE_DIR, file_name='image_python', extension=Types.PNG
    )
    IMAGE_PLAYWRIGHT: FilePath = generate_path(
        directory=TestDataDir.IMAGE_DIR, file_name='image_playwright', extension=Types.PNG
    )
    IMAGE_SELENIUM: FilePath = generate_path(
        directory=TestDataDir.IMAGE_DIR, file_name='image_selenium', extension=Types.PNG
    )
    IMAGE_HTTPX: FilePath = generate_path(directory=TestDataDir.IMAGE_DIR, file_name='image_httpx', extension=Types.PNG)
    IMAGE_PYTEST: FilePath = generate_path(
        directory=TestDataDir.IMAGE_DIR, file_name='image_pytest', extension=Types.PNG
    )

    ENVIRONMENT_PROPERTIES: FilePath = generate_path(
        directory=TestDataDir.ALLURE_RESULTS_DIR, file_name='environment.properties', extension=None
    )
    CATEGORIES_JSON: FilePath = generate_path(
        directory=TestDataDir.ALLURE_RESULTS_DIR, file_name='categories', extension=Types.JSON
    )

    # ENVIRONMENT_PROPERTIES: FilePath = TestDataDir.ALLURE_RESULTS_DIR.joinpath('environment.properties')
    # CATEGORIES_JSON: FilePath = TestDataDir.ALLURE_RESULTS_DIR.joinpath('categories.json')
