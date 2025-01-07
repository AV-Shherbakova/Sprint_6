import time

from selenium import webdriver

from conftest import BASE_URL
from locators.home_page_locators import ORDER_LOCATOR, LOGO_SCOOTER_BUTTON
from page_objects.home_page import HomePage


class TestRedirect:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    def test_redirect_home(self):
        self.driver.get(BASE_URL)
        home_page = HomePage(self.driver)
        home_page.click_order_button(ORDER_LOCATOR)
        self.driver.find_element(*LOGO_SCOOTER_BUTTON).click()
        time.sleep(0.5)
        assert self.driver.current_url == BASE_URL

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
