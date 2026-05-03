from pydantic import HttpUrl
from pydantic_settings import BaseSettings

from testdata.settings.browsers import Browsers


class BrowsersSettings(BaseSettings):
    """
    Описание структуры настроек браузеров.
    """

    app_url: HttpUrl
    headless: bool
    browsers: list[Browsers]
    width: int = 1920
    height: int = 1080
