import allure
from playwright.sync_api import Page

from testdata.allure.substeps import AllureSubstep
from ui_course.base_class import BaseClass
from ui_course.elements.button.button import Button
from ui_course.elements.text.text import Text


class ModalComponent(BaseClass):
    def __init__(self, page: Page, step: str):
        super().__init__(page)

        self.substep: str = AllureSubstep.MODAL
        self.step = self.generate_step(step=step)

        self.title = Text(page=page, locator='modal-title-text', name=f'Заголовок ({self.substep})', step=self.step)
        self.message = Text(
            page=page, locator='//div[@role="dialog"]//p', name=f'Сообщение ({self.substep})', step=self.step
        )
        self.button_x = Button(page=page, locator='modal-close-button', name=f'X ({self.substep})', step=self.step)
        self.button_cancel = Button(
            page=page, locator='modal-cancel-button', name=f'Cancel ({self.substep})', step=self.step
        )
        self.button_confirm = Button(
            page=page, locator='modal-confirm-button', name=f'Confirm ({self.substep})', step=self.step
        )

    def check_visible_status(self, status: bool = True, title: str | None = None, message: str | None = None):
        with allure.step(
            '{step}Проверить {status} модального окна'.format(
                step=self.step, status='отображение' if status else 'отсутствие'
            )
        ):
            self.title.check.visible_status(status=status)
            self.message.check.visible_status(status=status)
            self.message.check.visible_status(status=status)

            if status:
                if title is not None:
                    self.title.check.have_text(text=title)
                if message is not None:
                    self.message.check.have_text(text=message)

    def click_x_button(self):
        with allure.step(f'{self.step}Нажать X'):
            self.button_x.action.click()

    def click_cancel_button(self):
        with allure.step(f'{self.step}Нажать Cancel'):
            self.button_cancel.action.click()

    def click_confirm_button(self):
        with allure.step(f'{self.step}Нажать Confirm'):
            self.button_confirm.action.click()
