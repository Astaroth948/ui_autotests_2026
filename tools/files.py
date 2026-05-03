import json
import os

from pydantic import DirectoryPath, FilePath

from testdata.settings.types import Types


def generate_path(directory: DirectoryPath, file_name: str, extension: Types | None = None) -> FilePath:
    """
    Функция генерирует путь к файлу.

    :param directory: Директория файла.
    :param file_name: Имя файла.
    :param optional extension: Расширение файла.
    :return: Путь к файлу в формате `FilePath`.
    """

    if extension is not None:
        file_name += f'.{extension}'
    return directory.joinpath(file_name)


def get_list_files(directory: DirectoryPath, file_type: str, name_substring: str | None = None) -> list:
    """
    Функция ищет все файлы в директории с указанными построкой в названии и расширением.

    :param directory: Директория поиска.
    :param file_type: Расширение файла.
    :param optional name_substring: Подстрока в названии файла для поиска.
    :return: Список путей к файлам.
    """

    list_files = []
    if name_substring is None:
        name_substring = ""

    for filename in os.listdir(directory):
        if filename.endswith(file_type) and name_substring in filename:
            filepath = os.path.join(directory, filename)
            list_files.append(filepath)

    return list_files


def get_json_file(filepath: FilePath) -> dict:
    """
    Функция открывает и считывает данные из файла .json.

    :param filepath: Путь к файлу.
    :return: Данные .json файла в формате dict.
    """

    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def update_json_file(filepath: FilePath, data: dict):
    """
    Функция изменяет данные в файле .json или создает новый.

    :param filepath: Путь к файлу.
    :param data: Данные, которые необходимо записать в файл.
    """

    with open(filepath, 'w+', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def update_file(filepath: FilePath, data: str):
    """
    Функция изменяет данные в файле или создает новый.

    :param filepath: Путь к файлу.
    :param data: Данные, которые необходимо записать в файл.
    """

    with open(filepath, 'w+') as file:
        file.write(data)


def clear_directories(directories: list[DirectoryPath]):
    """
    Функция очищает список директорий.

    :param directories: Список директорий.
    """

    for dir in directories:
        for file in os.listdir(dir):
            os.remove(dir.joinpath(file))
