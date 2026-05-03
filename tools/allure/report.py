from pydantic import DirectoryPath

from config import settings
from testdata.directories import TestDataDir
from tools.files import get_json_file, get_list_files, update_json_file


def _get_fixture_name(directory: DirectoryPath, uuid: str) -> str:
    """
    Функция получает имя фикстуры по его uuid.

    :param directory: Директория поиска.
    :param uuid: Uuid фикстуры.
    :return: Имя фикстуры в формате str.
    """
    list_files = get_list_files(directory=directory, file_type='.json', name_substring='container')
    for filepath in list_files:
        data_allure_file = get_json_file(filepath=filepath)
        if data_allure_file['uuid'] == uuid:
            return data_allure_file['befores'][0]['name']


def _get_fixture_scope(fixture_name: str) -> str:
    """
    Функция получает scope фикстуры из ее имени.

    :param fixture_name: Имя фикстуры.
    :return: Scope фикстуры в формате str.
    """
    fixtures_scope = ['session', 'class', 'module']
    for scope in fixtures_scope:
        if scope in fixture_name:
            return scope
    return 'function'


def _get_linked_tests_by_statuses_fixtures(directory: DirectoryPath, statuses: list = ['failed', 'broken']) -> dict:
    """
    Функция получает связанные тесты с фикстурами по статусами.

    :param directory: Директория поиска.
    :param statuses: Список статусов.
    :return: Связанные тесты в формате dict {uuid фикстуры: [список uuid тестов]}
    """
    list_files = get_list_files(directory=directory, file_type='.json', name_substring='container')
    fixtures_dict = {}
    for filepath in list_files:
        data_allure_file = get_json_file(filepath=filepath)

        if (
            'children' in data_allure_file
            and len(data_allure_file['children']) > 1
            and 'befores' in data_allure_file
            and _get_fixture_scope(fixture_name=data_allure_file['befores'][0]['name']) != 'function'
        ):
            if data_allure_file['befores'][0]['status'] in statuses or (
                'afters' in data_allure_file and data_allure_file['afters'][0]['status'] in statuses
            ):
                fixtures_dict[data_allure_file['uuid']] = data_allure_file['children']
    return fixtures_dict


def _get_tests_files_by_uuid(directory: DirectoryPath, uuid_tests: list) -> list:
    """
    Функция получает пути тестов списку uuid.

    :param directory: Директория поиска.
    :param uuid_tests: Список uuid.
    :return: Пути тестов в формате list.
    """
    list_files = get_list_files(directory=directory, file_type='.json', name_substring='result')
    list_tests_files = []
    for filepath in list_files:
        data_allure_file = get_json_file(filepath=filepath)
        if data_allure_file['uuid'] in uuid_tests:
            list_tests_files.append(filepath)
    return list_tests_files


def _get_fixtures_tests_path_dict(directory: DirectoryPath, fixtures_dict: dict) -> dict:
    """
    Функция получает пути связанных тестов с фикстурами.

    :param directory: Директория поиска.
    :param fixtures_dict: Словарь в формате {uuid фикстуры: [список uuid тестов]}.
    :return: Связанные тесты в формате dict {uuid фикстуры: [пути связанных тестов]}
    """
    fixtures_tests_dict = fixtures_dict.copy()
    for fixture in fixtures_tests_dict.keys():
        fixtures_tests_dict[fixture] = _get_tests_files_by_uuid(directory=directory, uuid_tests=fixtures_dict[fixture])
    return fixtures_tests_dict


def _get_attachments_fixture(fixture_name: str, list_tests: list) -> list:
    """
    Функция получает получает аттачи фикстуры.

    :param fixture_name: Имя фикстуры.
    :param list_tests: Список путей к связанным тестам.
    :return: Аттачи фикстуры в формате list.
    """
    attachments_list = []

    for filepath in list_tests:
        data_allure_file = get_json_file(filepath=filepath)
        if 'attachments' in data_allure_file.keys():
            for attachment in data_allure_file['attachments']:
                if fixture_name in attachment['name']:
                    attachments_list.append(attachment)
    return attachments_list


def _get_fixtures_tests_attachments_dict(directory: DirectoryPath, fixtures_dict: dict) -> dict:
    """
    Функция получает аттачи связанных тестов с фикстурой.

    :param directory: Директория поиска.
    :param fixtures_dict: Словарь в формате {uuid фикстуры: [пути связанных тестов]}.
    :return: Аттачи фикстуры в формате list.
    """
    fixtures_tests_attachments_dict = fixtures_dict.copy()
    for fixture in fixtures_tests_attachments_dict.keys():
        fixtures_tests_attachments_dict[fixture] = _get_attachments_fixture(
            fixture_name=_get_fixture_name(directory=directory, uuid=fixture), list_tests=fixtures_dict[fixture]
        )
    return fixtures_tests_attachments_dict


def _update_attachments_fixtures(fixtures_dict: dict, fixtures_attachments_dict: dict):
    """
    Функция прикрепляет аттачи фикстур в те тесты, где их нет.

    :param fixtures_dict: Словарь с фикстурами и связанными путями тестов где они вызываются.
    :param fixtures_attachments_dict: Словарь с фикстурами и связанными аттачами.
    """
    for fixture in fixtures_dict.keys():
        for filepath in fixtures_dict[fixture]:
            data_allure_file = get_json_file(filepath=filepath)
            if 'attachments' not in data_allure_file.keys():
                data_allure_file.update({'attachments': fixtures_attachments_dict[fixture]})
                update_json_file(filepath=filepath, data=data_allure_file)
            else:
                current_attachments_list = []
                for current_attachment in data_allure_file['attachments']:
                    current_attachments_list.append(current_attachment['name'])
                for attachment in fixtures_attachments_dict[fixture]:
                    if attachment['name'] not in current_attachments_list:
                        data_allure_file['attachments'].append(attachment)
                        update_json_file(filepath=filepath, data=data_allure_file)


def _get_links_data_issues(data_allure_file: dict) -> tuple:
    """
    Функция получает имена и url ссылок из словаря.

    :param data_allure_file: Данные .json файла в формате dict.
    :return: Имена и url ссылок в формате tuple.
    """
    name_list = []
    url_list = []
    if 'links' in data_allure_file.keys():
        for link_data in data_allure_file['links']:
            name_list.append(link_data['name'])
            url_list.append(link_data['url'])

    return '\n\n'.join(name_list), '\n\n'.join(url_list)


def _update_status_details_test_result(data_allure_file: dict) -> dict:
    """
    Функция прописывает пустые строки в детали статуса message и trace.
    Это необходимо для кастомных категорий.

    :param data_allure_file: Данные .json файла в формате dict.
    :return: Измененный .json файл в формате dict.
    """
    message = (
        data_allure_file['statusDetails']['message']
        if 'statusDetails' in data_allure_file and 'message' in data_allure_file['statusDetails']
        else ''
    )
    trace = (
        data_allure_file['statusDetails']['trace']
        if 'statusDetails' in data_allure_file and 'trace' in data_allure_file['statusDetails']
        else ''
    )

    data_allure_file.update({'statusDetails': {'message': message, 'trace': trace}})
    return data_allure_file


def _update_status_test_result(data_allure_file: dict, links_name: str, links_url: str) -> dict:
    """
    Функция прописывает имена и url ссылок в сообщение об ошибке.
    В зависимости от настроек, меняет статусы результата теста для читаемости отчета.

    :param data_allure_file: Данные .json файла в формате dict.
    :param links_name: Строка с именами ссылок.
    :param links_url: Строка с url ссылок.
    :return: Измененный .json файл в формате dict.
    """
    data_allure_file = _update_status_details_test_result(data_allure_file=data_allure_file)
    if 'links' in data_allure_file.keys():
        status = data_allure_file['status']
        message = data_allure_file['statusDetails']['message']
        trace = data_allure_file['statusDetails']['trace']
        if status == 'passed':
            if settings.allure_settings.custom_report:
                status = 'broken'
            message = links_name
            trace = links_url
        elif status == 'failed':
            if settings.allure_settings.custom_report:
                status = 'unknown'
            message = links_name + '\n\n' + message
            trace = links_url + '\n\n' + trace
        data_allure_file.update({'status': status, 'statusDetails': {'message': message, 'trace': trace}})
    return data_allure_file


def _update_tags_report(data_allure_file: dict) -> dict:
    """
    Функция преобразовывает Pytest теги в формат UPPER_SNAKE_CASE

    :param data_allure_file: Данные .json файла в формате dict.
    :return: Измененный .json файл в формате dict.
    """
    if 'labels' in data_allure_file.keys():
        list_labels = []

        for tag_data in data_allure_file['labels']:
            if tag_data['name'] == 'tag':
                tag_data['value'] = tag_data['value'].upper()
            list_labels.append(tag_data)
        data_allure_file.update({'labels': list_labels})
    return data_allure_file


def attach_attachments_fail_fixtures_tests(directory: DirectoryPath = TestDataDir.ALLURE_RESULTS_DIR):
    """
    Функция находит все файлы с результатами allure,
    прикрепляет недостающие аттачи при падении фикстур со scope [class, module, session].
    Изначально аттачи прикрепляются только к одному тесту при падении подобных фикстур.

    :param directory: Директория поиска.
    """
    fail_fixtures = _get_linked_tests_by_statuses_fixtures(directory=directory, statuses=['failed', 'broken'])
    fail_fixtures_tests = _get_fixtures_tests_path_dict(directory=directory, fixtures_dict=fail_fixtures)
    fail_fixtures_tests_attachments = _get_fixtures_tests_attachments_dict(
        directory=directory, fixtures_dict=fail_fixtures_tests
    )
    _update_attachments_fixtures(
        fixtures_dict=fail_fixtures_tests, fixtures_attachments_dict=fail_fixtures_tests_attachments
    )


def generate_custom_report(directory: DirectoryPath = TestDataDir.ALLURE_RESULTS_DIR):
    """
    Функция находит все файлы с результатами allure,
    прописывает имена и url ссылок в сообщение об ошибке где они есть.
    В зависимости от настроек, меняет статусы результатов тестов для читаемости отчета.

    :param directory: Директория поиска.
    """
    list_files = get_list_files(directory=directory, file_type='.json', name_substring='result')
    for filepath in list_files:
        data_allure_file = get_json_file(filepath=filepath)
        links_name, links_url = _get_links_data_issues(data_allure_file=data_allure_file)
        data_allure_file = _update_status_test_result(
            data_allure_file=data_allure_file, links_name=links_name, links_url=links_url
        )
        update_json_file(filepath=filepath, data=data_allure_file)


def format_tags_report(directory: DirectoryPath = TestDataDir.ALLURE_RESULTS_DIR):
    """
    Функция находит все файлы с результатами allure,
    преобразовывает Pytest теги в формат UPPER_SNAKE_CASE.

    :param directory: Директория поиска.
    """
    list_files = get_list_files(directory=directory, file_type='.json', name_substring='result')
    for filepath in list_files:
        data_allure_file = get_json_file(filepath=filepath)
        data_allure_file = _update_tags_report(data_allure_file=data_allure_file)
        update_json_file(filepath=filepath, data=data_allure_file)
