from pydantic import DirectoryPath


class TestDataDir:
    """
    Класс для хранения путей директорий.
    """

    ALLURE_RESULTS_DIR: DirectoryPath = DirectoryPath('./allure-results')
    ARTIFACTS_DIR: DirectoryPath = DirectoryPath('./artifacts')
    SCREEN_DIR: DirectoryPath = ARTIFACTS_DIR.joinpath('screen')
    VIDEOS_DIR: DirectoryPath = ARTIFACTS_DIR.joinpath('videos')
    TRACING_DIR: DirectoryPath = ARTIFACTS_DIR.joinpath('tracing')
    BROWSER_STATE_DIR: DirectoryPath = DirectoryPath('./testdata/files/browser_state')
    IMAGE_DIR: DirectoryPath = DirectoryPath('./testdata/files/images')

    def create_required_directories(self):
        """
        Функция создает все необходимые директории.
        """

        self.ALLURE_RESULTS_DIR.mkdir(exist_ok=True)
        self.ARTIFACTS_DIR.mkdir(exist_ok=True)
        self.SCREEN_DIR.mkdir(exist_ok=True)
        self.VIDEOS_DIR.mkdir(exist_ok=True)
        self.TRACING_DIR.mkdir(exist_ok=True)
        self.BROWSER_STATE_DIR.mkdir(exist_ok=True)
        self.IMAGE_DIR.mkdir(exist_ok=True)
