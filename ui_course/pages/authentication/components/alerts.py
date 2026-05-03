import allure
from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from testdata.text import AlertsText
from ui_course.base_class import BaseClass
from ui_course.elements.text.text import Text


class AuthAlerts(BaseClass):
    def __init__(self, page: Page, step: str):
        super().__init__(page)

        self.substep: str = AllureSubstep.ALERTS
        self.step = self.generate_step(step=step)

        self.wrong_email_or_password_alert = Text(
            page=page, locator='login-page-wrong-email-or-password-alert', name=f'Алерт {self.substep}', step=self.step
        )

    def check_visible_status_wrong_email_or_password_alert(self, status: bool = True):
        with allure.step(
            '{step}Проверить {status} алерта "{alert}"'.format(
                step=self.step,
                status='отображение' if status else 'отсутствие',
                alert=AlertsText.WRONG_EMAIL_OR_PASSWORD,
            )
        ):
            self.wrong_email_or_password_alert.check.visible_status(status=status)
            if status:
                self.wrong_email_or_password_alert.check.have_text(text=AlertsText.WRONG_EMAIL_OR_PASSWORD)
