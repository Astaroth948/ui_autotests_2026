from pydantic import BaseModel, Field, FilePath


class CourseEditorMainFormModel(BaseModel):
    course_title: str = ''
    estimated_time: str = ''
    description: str = ''
    max_score: str = '0'
    min_score: str = '0'


class CourseEditorExercisesFormModel(BaseModel):
    exercise_title: str = 'Exercise title'
    description: str = 'Exercise description'


class CourseEditorModel(BaseModel):
    image_file: FilePath | None
    main_form: CourseEditorMainFormModel
    exercises_form: list[CourseEditorExercisesFormModel] = []


class CourseCardModel(CourseEditorMainFormModel):
    description: str = Field(exclude=True, default='')
