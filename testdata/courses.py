from testdata.files.files import TestDataFiles
from ui_course.pages.courses.models import CourseEditorExercisesFormModel, CourseEditorMainFormModel, CourseEditorModel


class CourseMainFormData:
    """
    Класс для хранения тестовых данных главной панели курсов.
    """

    DEFAULT_MAIN_FORM = CourseEditorMainFormModel()
    COURSE_PYTHON = CourseEditorMainFormModel(
        course_title='Python',
        max_score='100',
        min_score='10',
        description='Python description',
        estimated_time='2 weeks',
    )
    COURSE_PLAYWRIGHT = CourseEditorMainFormModel(
        course_title='Playwright',
        max_score='300',
        min_score='50',
        description='Playwright description',
        estimated_time='2 month',
    )
    COURSE_SELENIUM = CourseEditorMainFormModel(
        course_title='Selenuim',
        max_score='200',
        min_score='30',
        description='Selenuim description',
        estimated_time='1 month',
    )
    COURSE_HTTPX = CourseEditorMainFormModel(
        course_title='HTTPX', max_score='400', min_score='60', description='HTTPX description', estimated_time='3 weeks'
    )
    COURSE_PYTEST = CourseEditorMainFormModel(
        course_title='Pytest',
        max_score='250',
        min_score='35',
        description='Pytest description',
        estimated_time='1 month 2 weeks',
    )


class CourseExercisesFormData:
    """
    Класс для хранения тестовых данных панели заданий.
    """

    DEFAULT_EXERCISE_FORM = CourseEditorExercisesFormModel(
        exercise_title='Exercise title', description='Exercise description'
    )

    COURSE_PYTHON_EXERCISE_1 = CourseEditorExercisesFormModel(
        exercise_title='Python title exercise 1', description='Python exercise description 1'
    )
    COURSE_PYTHON_EXERCISE_2 = CourseEditorExercisesFormModel(
        exercise_title='Python title exercise 2', description='Python exercise description 2'
    )

    COURSE_PLAYWRIGHT_EXERCISE_1 = CourseEditorExercisesFormModel(
        exercise_title='Playwright title exercise 1', description='Playwright exercise description 1'
    )
    COURSE_PLAYWRIGHT_EXERCISE_2 = CourseEditorExercisesFormModel(
        exercise_title='Playwright title exercise 1', description='Playwright exercise description 2'
    )
    COURSE_PLAYWRIGHT_EXERCISE_3 = CourseEditorExercisesFormModel(
        exercise_title='Playwright title exercise 1', description='Playwright exercise description 3'
    )

    COURSE_SELENIUM_EXERCISE_1 = CourseEditorExercisesFormModel(
        exercise_title='Selenuim title exercise 1', description='Selenuim exercise description 1'
    )

    COURSE_PYTEST_EXERCISE_1 = CourseEditorExercisesFormModel(
        exercise_title='Selenuim title exercise 1', description='Pytest exercise description 1'
    )
    COURSE_PYTEST_EXERCISE_2 = CourseEditorExercisesFormModel(
        exercise_title='Selenuim title exercise 2', description='Pytest exercise description 2'
    )
    COURSE_PYTEST_EXERCISE_3 = CourseEditorExercisesFormModel(
        exercise_title='Selenuim title exercise 3', description='Pytest exercise description 3'
    )
    COURSE_PYTEST_EXERCISE_4 = CourseEditorExercisesFormModel(
        exercise_title='Selenuim title exercise 4', description='Pytest exercise description 4'
    )


class CourseEditorData:
    """
    Класс для хранения тестовых данных редактора курсов.
    """

    COURSE_EMPTY = CourseEditorModel(image_file=None, main_form=CourseMainFormData.DEFAULT_MAIN_FORM, exercises_form=[])
    COURSE_PYTHON = CourseEditorModel(
        image_file=TestDataFiles.IMAGE_PYTHON,
        main_form=CourseMainFormData.COURSE_PYTHON,
        exercises_form=[
            CourseExercisesFormData.COURSE_PYTHON_EXERCISE_1,
            CourseExercisesFormData.COURSE_PYTHON_EXERCISE_2,
        ],
    )
    COURSE_PLAYWRIGHT = CourseEditorModel(
        image_file=TestDataFiles.IMAGE_PLAYWRIGHT,
        main_form=CourseMainFormData.COURSE_PLAYWRIGHT,
        exercises_form=[
            CourseExercisesFormData.COURSE_PLAYWRIGHT_EXERCISE_1,
            CourseExercisesFormData.COURSE_PLAYWRIGHT_EXERCISE_2,
            CourseExercisesFormData.COURSE_PLAYWRIGHT_EXERCISE_3,
        ],
    )
    COURSE_SELENIUM = CourseEditorModel(
        image_file=TestDataFiles.IMAGE_SELENIUM,
        main_form=CourseMainFormData.COURSE_SELENIUM,
        exercises_form=[CourseExercisesFormData.COURSE_SELENIUM_EXERCISE_1],
    )
    COURSE_HTTPX = CourseEditorModel(
        image_file=TestDataFiles.IMAGE_HTTPX, main_form=CourseMainFormData.COURSE_HTTPX, exercises_form=[]
    )
    COURSE_PYTEST = CourseEditorModel(
        image_file=TestDataFiles.IMAGE_PYTEST,
        main_form=CourseMainFormData.COURSE_PYTEST,
        exercises_form=[
            CourseExercisesFormData.COURSE_PYTEST_EXERCISE_1,
            CourseExercisesFormData.COURSE_PYTEST_EXERCISE_2,
            CourseExercisesFormData.COURSE_PYTEST_EXERCISE_3,
            CourseExercisesFormData.COURSE_PYTEST_EXERCISE_4,
        ],
    )


"""
Список для хранения тестовых данных при создании и проверках нескольких курсов.
"""
PRECONDITION_COURSES_LIST = [
    CourseEditorData.COURSE_PYTHON.main_form,
    CourseEditorData.COURSE_PLAYWRIGHT.main_form,
    CourseEditorData.COURSE_SELENIUM.main_form,
]
