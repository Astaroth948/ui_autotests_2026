import pytest

from tools.allure.categories import create_allure_categories_file
from tools.allure.environment import create_allure_environment_file


@pytest.fixture(scope='session', autouse=True)
def save_allure_files():
    """
    Фикстура для создания allure файлов environment.properties и categories.json.

    :scope: session.
    """

    yield
    create_allure_environment_file()
    create_allure_categories_file()
