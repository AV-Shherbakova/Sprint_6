import time

from conftest import scroll_to_element
from locators.home_page_locators import *


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def click_question_and_return_text(self, index):
        questions_block = self.driver.find_element(*QUESTIONS_LOCATOR)
        scroll_to_element(self.driver, questions_block)
        accordion_items = self.driver.find_elements(*ACCORDION_ITEM_LOCATOR)
        time.sleep(0.05)
        item_to_click = accordion_items[index]
        item_to_click.click()
        panel = item_to_click.find_element(*ACCORDION_PANEL_LOCATOR)
        return panel.text

    def click_order_button(self, locator):
        order_button = self.driver.find_element(*locator)
        scroll_to_element(self.driver, order_button)
        time.sleep(0.05)
        order_button.click()
