from pages.demo_qa_base_page import DemoQaBasePage
from playwright.sync_api import Page


class DemoQaMainPage(DemoQaBasePage):
    _option_list = '.category-cards .card'
    _home_page_image_caption = '.banner-image'

    def __int__(self, page: Page):
        super().__int__(page)

    def choose_option_from_main_page(self, option_name: str):
        self.choose_item_by_name(self._option_list, option_name)

    def get_home_page_image_caption(self, text):
        return self.get_inner_text(self._home_page_image_caption)