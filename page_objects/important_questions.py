import time

from selenium.webdriver.common.by import By


class ImportantQuestions:
    questions_locator = [By.CLASS_NAME, 'Home_FourPart__1uthg']
    accordion_item_locator = [By.CLASS_NAME, 'accordion__item']
    accordion_panel_locator = [By.CLASS_NAME, 'accordion__panel']

    def __init__(self, driver):
        self.driver = driver

    def click_element_and_return_hidden(self, index):
        questions_block = self.driver.find_element(*self.questions_locator)
        self.scroll_to_element(questions_block)
        accordion_items = self.driver.find_elements(*self.accordion_item_locator)
        time.sleep(0.05)
        item_to_click = accordion_items[index]
        item_to_click.click()
        panel = item_to_click.find_element(*self.accordion_panel_locator)
        return panel.text

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
