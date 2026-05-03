import re
from typing import Pattern

import allure
from playwright.sync_api import Page, expect

from ui_course.base_class import BaseClass


class BasePage(BaseClass):
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        with allure.step(f'{self.step}Открыть URL "{url}"'):
            self.page.goto(url, wait_until='networkidle')

    def reload(self):
        with allure.step(f'{self.step}Перезагрузить страницу с URL "{self.page.url}"'):
            self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, expected_url: Pattern[str] | str):
        with allure.step(f'{self.step}Проверить что текущий URL содержит {expected_url}'):
            expect(self.page).to_have_url(re.compile(expected_url))
