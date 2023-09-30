from pages.demo_qa_base_page import DemoQaBasePage
from playwright.sync_api import Page


class AccordianPanelsPage(DemoQaBasePage):
    _side_bar_panel = '.accordion .group-header'

    def __int__(self, page: Page):
        super().__int__(page)

    def choose_panel_category(self, panel_name: str):
        self.choose_item_by_name()

