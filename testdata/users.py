from config import settings
from ui_course.pages.authentication.models import UserModel


class UsersData:
    """
    Класс для хранения тестовых пользователей.
    """

    EMPTY_FORM = UserModel()
    DEFAULT_USER = settings.test_user
