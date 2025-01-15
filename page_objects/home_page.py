from locators.home_page_locators import *
from page_objects.page import Page


class HomePage(Page):

    def click_question_and_return_text(self, index):
        questions_block = self.find_element_by_locator(QUESTIONS_LOCATOR)
        self.scroll_to_element(questions_block)
        accordion_items = self.find_elements_by_locator(ACCORDION_ITEM_LOCATOR)
        self.wait()
        item_to_click = accordion_items[index]
        self.click_element(item_to_click)
        panel = item_to_click.find_element(*ACCORDION_PANEL_LOCATOR)
        return panel.text

    def click_order_button(self, locator):
        order_button = self.find_element_by_locator(locator)
        self.scroll_to_element(order_button)
        self.wait()
        self.click_element(order_button)

    def click_zen_button(self):
        self.find_and_click_element(LOGO_YANDEX_BUTTON)
