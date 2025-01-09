import time

from conftest import driver
from locators.home_page_locators import ORDER_LOCATOR, LOGO_SCOOTER_BUTTON
from page_objects.home_page import HomePage
from urls import BASE_URL, ZEN_URL


class TestRedirect:

    def test_redirect_home(self, driver):
        driver.get(BASE_URL)
        home_page = HomePage(driver)
        home_page.click_order_button(ORDER_LOCATOR)
        home_page.find_and_click_element(LOGO_SCOOTER_BUTTON)
        home_page.wait()
        assert driver.current_url == BASE_URL

    def test_redirect_zen(self, driver):
        driver.get(BASE_URL)
        home_page = HomePage(driver)
        home_page.click_zen_button()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == ZEN_URL
