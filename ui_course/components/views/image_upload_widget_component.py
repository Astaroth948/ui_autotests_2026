import allure
from playwright.sync_api import Page
from pydantic import FilePath

from testdata.allure.substeps import AllureSubstep
from testdata.text import EmptyViewText, ImageUploadWidgetText
from ui_course.base_class import BaseClass
from ui_course.components.views.empty_view_component import EmptyViewComponent
from ui_course.elements.button.button import Button
from ui_course.elements.file_input.file_input import FileInput
from ui_course.elements.icon.icon import Icon
from ui_course.elements.image.image import Image
from ui_course.elements.text.text import Text


class ImageUploadWidgetComponent(BaseClass):
    def __init__(self, page: Page, identifier: str, step: str):
        super().__init__(page)

        self.substep: str = AllureSubstep.IMAGE_UPLOAD_WIDGET
        self.step = self.generate_step(step=step)

        self.preview_empty_view = EmptyViewComponent(page=page, identifier=identifier, step=self.step)
        self.preview_image = Image(
            page=page,
            locator=f'{identifier}-image-upload-widget-preview-image',
            name=f'Превью ({self.substep})',
            step=self.step,
        )

        self.image_upload_info_icon = Icon(
            page=page,
            locator=f'{identifier}-image-upload-widget-info-icon',
            name=f'Upload info ({self.substep})',
            step=self.step,
        )
        self.image_upload_info_title = Text(
            page=page,
            locator=f'{identifier}-image-upload-widget-info-title-text',
            name=f'Заголовок Upload info ({self.substep})',
            step=self.step,
        )
        self.image_upload_info_description = Text(
            page=page,
            locator=f'{identifier}-image-upload-widget-info-description-text',
            name=f'Описание Upload info ({self.substep})',
            step=self.step,
        )

        self.upload_button = Button(
            page=page,
            locator=f'{identifier}-image-upload-widget-upload-button',
            name=f'Upload ({self.substep})',
            step=self.step,
        )
        self.remove_button = Button(
            page=page,
            locator=f'{identifier}-image-upload-widget-remove-button',
            name=f'Remove ({self.substep})',
            step=self.step,
        )
        self.upload_input = FileInput(
            page=page,
            locator=f'{identifier}-image-upload-widget-input',
            name=f'Форма загрузки файла ({self.substep})',
            step=self.step,
        )

    def _check_visible_text_info_panel(self):
        self.image_upload_info_icon.check.visible_status(status=True)

        self.image_upload_info_title.check.visible_status(status=True)
        self.image_upload_info_title.check.have_text(text=ImageUploadWidgetText.INFO_TITLE)

        self.image_upload_info_description.check.visible_status(status=True)
        self.image_upload_info_description.check.have_text(text=ImageUploadWidgetText.INFO_DESCRIPTION)

    def _check_status_buttons_info_panel(self, is_image_uploaded: bool = False):
        self.upload_button.check.visible_status(status=True)
        self.remove_button.check.visible_status(status=is_image_uploaded)

    def _check_status_preview_image_panel(self, is_image_uploaded: bool = False):
        self.preview_image.check.visible_status(status=is_image_uploaded)
        self.preview_empty_view.check_visible_status(
            status=not is_image_uploaded,
            title=EmptyViewText.NO_IMAGE_TITLE,
            description=EmptyViewText.NO_IMAGE_DESCRIPTION,
        )

    def check_visible_status_widget(self, is_image_uploaded: bool = False):
        with allure.step(
            '{step}Проверить состояние виджета при {image_status} изображения'.format(
                step=self.step, image_status='наличии' if is_image_uploaded else 'отсутствии'
            )
        ):
            self._check_visible_text_info_panel()

            self._check_status_preview_image_panel(is_image_uploaded=is_image_uploaded)
            self._check_status_buttons_info_panel(is_image_uploaded=is_image_uploaded)

    def click_remove_image_button(self):
        with allure.step(f'{self.step}Нажать на кнопку "Remove"'):
            self.remove_button.action.click()

    def upload_preview_image(self, file: FilePath):
        with allure.step(f'{self.step}Загрузить изображение "{file}"'):
            self.upload_input.action.set_input_files(file=file)

    def get_visible_status_preview_image(self) -> bool:
        with allure.step(f'{self.step}Получить статус отображения превью картинки'):
            return self.preview_image.action.get_visible_status()

    def remove_preview_image(self):
        with allure.step(f'{self.step}Удалить превью изображение'):
            if self.get_visible_status_preview_image():
                self.click_remove_image_button()
