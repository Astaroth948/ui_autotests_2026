from pydantic import BaseModel


class AllureSettings(BaseModel):
    """
    Описание структуры настроек allure отчета.
    """

    screens: bool = True
    videos: bool = True
    tracing: bool = True
    custom_steps: bool = True
    custom_report: bool = True
    clear_reports_at_start: bool = False
    issue_masks: list[str] = ["UI", "API"]
