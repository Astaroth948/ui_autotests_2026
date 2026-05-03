from config import settings
from testdata.files.files import TestDataFiles
from tools.files import update_file


def create_allure_environment_file():
    """
    Функция генерирует и создает environment.properties файл для отчета allure.
    """

    settings_dict = settings.model_dump()
    settings_list = []

    for key_settings, value_settings in settings_dict.items():
        if isinstance(value_settings, dict):
            settings_list.append(key_settings.upper() + '=')
            for nested_key, nested_value in value_settings.items():
                settings_list.append(str(nested_key) + '=' + str(nested_value))
        else:
            settings_list.append(key_settings.upper() + '=' + value_settings)

    properties = '\n'.join(settings_list)

    update_file(filepath=TestDataFiles.ENVIRONMENT_PROPERTIES, data=properties)
