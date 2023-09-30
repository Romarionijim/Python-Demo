from playwright.sync_api import Page
import datetime


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click_element(self, locator):
        if isinstance(locator, str):
            self.page.locator(locator).click()
        else:
            locator.click()

    def fill_text(self, locator, text: str):
        self.page.locator(locator).fill(text)

    def get_inner_text(self, locator):
        self.page.locator(locator).inner_text()

    def get_input_value(self, locator):
        self.page.locator(locator).input_value()

    def right_click(self, locator):
        self.page.locator(locator).click(button="right")

    def get_day(self):
        day = datetime.datetime.now().day
        return day

    def get_month(self):
        month = datetime.datetime.now().month
        return month

    def get_year(self):
        year = datetime.datetime.now().year
        return year

    def scroll_into_view_if_needed(self, locator):
        self.page.locator(locator).scroll_into_view_if_needed()

    def sleep(self, seconds: int):
        self.page.wait_for_timeout(seconds)

    def wait_for_visibility_of_element(self, locator):
        self.page.locator(locator).wait_for(state="visible")

    def select_option(self, locator, value=None, label=None):
        if value is not None:
            self.page.locator(locator).select_option(value=value)
        elif label is not None:
            self.page.locator(locator).select_option(label=label)
        else:
            raise ValueError("none of the conditions in the select option function were satisfied")
