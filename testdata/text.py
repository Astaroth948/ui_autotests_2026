from enum import StrEnum


class HeaderText(StrEnum):
    """
    Класс для хранения текстовок заголовков.
    """

    APP_TITLE: str = 'UI Course'
    WELCOME_TITLE: str = 'Welcome, {username}!'


class SidebarText(StrEnum):
    """
    Класс для хранения текстовок сайдбара.
    """

    LOGOUT: str = 'Logout'
    COURSES: str = 'Courses'
    DASHBOARD: str = 'Dashboard'


class ChartsText(StrEnum):
    """
    Класс для хранения текстовок диаграмм.
    """

    STUDENTS: str = 'Students'
    COURSES: str = 'Courses'
    ACTIVITIES: str = 'Activities'
    SCORES: str = 'Scores'


class EmptyViewText(StrEnum):
    """
    Класс для хранения текстовок компонента Empty View.
    """

    NO_IMAGE_TITLE: str = 'No image selected'
    NO_IMAGE_DESCRIPTION: str = 'Preview of selected image will be displayed here'

    NO_EXERCIES_TITLE: str = 'There is no exercises'
    NO_EXERCIES_DESCRIPTION: str = 'Click on "Create exercise" button to create new exercise'

    NO_COURSES_TITLE: str = 'There is no results'
    NO_COURSES_DESCRIPTION: str = 'Results from the load test pipeline will be displayed here'


class ImageUploadWidgetText(StrEnum):
    """
    Класс для хранения текстовок компонента Image Upload Widget.
    """

    INFO_TITLE: str = 'Tap on "Upload image" button to select file'
    INFO_DESCRIPTION: str = 'Recommended file size 540X300'


class CourseCardFieldsText(StrEnum):
    """
    Класс для хранения текстовок полей карточки курса.
    """

    MAX_SCORE: str = 'Max score: {max_score}'
    MIN_SCORE: str = 'Min score: {min_score}'
    ESTIMATED_TIME: str = 'Estimated time: {estimated_time}'


class ModalText(StrEnum):
    """
    Класс для хранения текстовок модальных окон.
    """

    DELETE_COURSE_TITLE: str = 'Confirm deleting course'
    DELETE_COURSE_MESSAGE: str = 'Are you sure you want to delete the course? This action cannot be undone'


class ToolbarText(StrEnum):
    """
    Класс для хранения текстовок тулбаров.
    """

    COURSES_TITLE: str = 'Courses'
    DASHBOARD_TITLE: str = 'Dashboard'


class CourseEditorText(StrEnum):
    """
    Класс для хранения текстовок редактора курсов.
    """

    CREATE_MODE_TITLE: str = 'Create course'
    UPDATE_MODE_TITLE: str = 'Update course'
    EXERCISES_TITLE: str = 'Exercises'
    EXERCISE_SUBTITLE: str = '#{index} Exercise'


class AlertsText(StrEnum):
    """
    Класс для хранения текстовок алертов.
    """

    WRONG_EMAIL_OR_PASSWORD: str = 'Wrong email or password'
