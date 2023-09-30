from pages.base_page import BasePage
from playwright.sync_api import Page


class DemoQaBasePage(BasePage):
    def __int__(self, page: Page):
        super().__init__(page)

    def get_order_of_elements(self, locator):
        elements_order: list = []
        element_list = self.page.locator(locator).all()
        for i in range(len(element_list)):
            element_inner_text = element_list[i].inner_text()
            elements_order.append(element_inner_text)
        return elements_order

    def choose_item_by_name(self, locator, item_name: str):
        item = self.page.locator(locator, has_text=item_name)
        self.click_element(item)

    def choose_from_list_by_text(self, locator, text: str):
        element_list = self.page.locator(locator).all()
        for element in element_list:
            element_inner_text = element.inner_text()
            if element_inner_text.strip() == text:
                element.click()
                break

    def click_on_desired_button_from_specific_item(self, locator, item_name: str, button_element:str):
        item = self.page.locator(locator, has_text=item_name)
        desired_button = item.locator(button_element)
        self.click_element(desired_button)

