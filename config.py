import os
import platform
import sys
from typing import Self

from pydantic_settings import BaseSettings, SettingsConfigDict

from testdata.directories import TestDataDir
from testdata.settings.allure_settings import AllureSettings
from testdata.settings.browsers_settings import BrowsersSettings
from ui_course.pages.authentication.models import UserModel


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f".env.{os.getenv('ENV', 'local')}", env_file_encoding='utf-8', env_nested_delimiter='.'
    )

    browsers_settings: BrowsersSettings
    allure_settings: AllureSettings
    test_user: UserModel
    os_info: str = ''
    python_version: str = ''

    @classmethod
    def initialize(cls) -> Self:
        directories = TestDataDir()
        directories.create_required_directories()

        os_info = f'{platform.system()}, {platform.release()}'
        python_version = sys.version

        return Settings(os_info=os_info, python_version=python_version)

    def get_base_url(self) -> str:
        return str(self.browsers_settings.app_url)


settings: Settings = Settings.initialize()
