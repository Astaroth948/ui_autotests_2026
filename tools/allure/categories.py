from enum import Enum, StrEnum

from pydantic import BaseModel, ConfigDict, Field

from config import settings
from testdata.files.files import TestDataFiles
from tools.files import update_json_file


class CategorySchema(BaseModel):
    """
    Описание структуры категории allure для файла categories.json.
    """

    model_config = ConfigDict(populate_by_name=True)

    name: str
    trace_regex: str | None = Field(alias='traceRegex', default=None)
    message_regex: str | None = Field(alias='messageRegex', default=None)
    matched_statuses: list[str] = Field(alias='matchedStatuses')


class CategoryStatus(StrEnum):
    """
    Класс для хранения статусов.
    """

    PASSED = "passed"
    BROKEN = "broken"
    SKIPPED = "skipped"
    FAILED = "failed"
    UNKNOWN = "unknown"


class CategoryName(StrEnum):
    """
    Класс для хранения названий категорий.
    """

    KNOWN_DEFECTS = "Заведенные дефекты"
    FIXED_DEFECTS = "Исправленные дефекты"
    NEW_DEFECTS = "Новые дефекты"

    PASSED_TESTS = "Успешные тесты"
    BROKEN_TESTS = "Сломанные тесты"
    SKIPPED_TESTS = "Пропущенные тесты"
    UNKNOWN_TESTS = "Неизвестные тесты"

    XFAIL = "XFAIL"
    XPASS = "XPASS"


class CategoryRegex(StrEnum):
    """
    Класс для хранения регулярных выражений категорий.
    """

    def mask() -> str:
        """
        Функция генерирует маску для регулярных выражений
        с идентификаторами заведенных задач для обнаруженных дефектов.
        """

        return '|'.join(settings.allure_settings.issue_masks)

    INCLUDE_MASK = f".*({mask()})-\\d+.*"
    NOT_INCLUDE_MASK = f"^(?!.*({mask()})-\\d+|(XPASS)|(XFAIL)).*$"
    XFAIL_MASK = ".*XFAIL.*"
    XPASS_MASK = ".*XPASS.*"


class CategoriesList(Enum):
    """
    Класс для хранения категорий.
    """

    XPASS = CategorySchema(
        name=CategoryName.XPASS, message_regex=CategoryRegex.XPASS_MASK, matched_statuses=[CategoryStatus.PASSED]
    )
    FIXED_DEFECTS = CategorySchema(
        name=CategoryName.FIXED_DEFECTS,
        trace_regex=CategoryRegex.INCLUDE_MASK,
        matched_statuses=[CategoryStatus.PASSED, CategoryStatus.BROKEN],
    )
    PASSED_TESTS = CategorySchema(
        name=CategoryName.PASSED_TESTS,
        trace_regex=CategoryRegex.NOT_INCLUDE_MASK,
        message_regex=CategoryRegex.NOT_INCLUDE_MASK,
        matched_statuses=[CategoryStatus.PASSED],
    )
    KNOWN_DEFECTS = CategorySchema(
        name=CategoryName.KNOWN_DEFECTS,
        trace_regex=CategoryRegex.INCLUDE_MASK,
        matched_statuses=[CategoryStatus.FAILED, CategoryStatus.SKIPPED, CategoryStatus.UNKNOWN],
    )
    NEW_DEFECTS = CategorySchema(
        name=CategoryName.NEW_DEFECTS,
        trace_regex=CategoryRegex.NOT_INCLUDE_MASK,
        message_regex=CategoryRegex.NOT_INCLUDE_MASK,
        matched_statuses=[CategoryStatus.FAILED],
    )
    BROKEN_TESTS = CategorySchema(
        name=CategoryName.BROKEN_TESTS,
        trace_regex=CategoryRegex.NOT_INCLUDE_MASK,
        message_regex=CategoryRegex.NOT_INCLUDE_MASK,
        matched_statuses=[CategoryStatus.BROKEN],
    )
    XFAIL = CategorySchema(
        name=CategoryName.XFAIL, message_regex=CategoryRegex.XFAIL_MASK, matched_statuses=[CategoryStatus.SKIPPED]
    )
    SKIPPED_TESTS = CategorySchema(
        name=CategoryName.SKIPPED_TESTS,
        trace_regex=CategoryRegex.NOT_INCLUDE_MASK,
        message_regex=CategoryRegex.NOT_INCLUDE_MASK,
        matched_statuses=[CategoryStatus.SKIPPED],
    )
    UNKNOWN_TESTS = CategorySchema(
        name=CategoryName.UNKNOWN_TESTS,
        trace_regex=CategoryRegex.NOT_INCLUDE_MASK,
        matched_statuses=[CategoryStatus.UNKNOWN],
    )

    @property
    def dict_value(self) -> dict:
        """
        Функция сериализует объект `CategorySchema` в словарь.

        :return: Результат сериализации объекта категории в виде словаря.
        """

        return self.value.model_dump(by_alias=True, exclude_none=True)


def create_allure_categories_file():
    """
    Функция сохраняет категории в файл categories.json.
    """

    categories_list = [category.dict_value for category in CategoriesList]
    update_json_file(filepath=TestDataFiles.CATEGORIES_JSON, data=categories_list)
