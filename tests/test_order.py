import pytest
from selenium import webdriver

from conftest import BASE_URL
from locators.home_page_locators import ORDER_LOCATOR_BIG, ORDER_LOCATOR
from page_objects.home_page import HomePage
from page_objects.order_page import OrderPage


class TestOrders:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @pytest.mark.parametrize(
        "locator",
        [
            ORDER_LOCATOR,
            ORDER_LOCATOR_BIG
        ]
    )
    @pytest.mark.parametrize(
        "name, surname, address, phone",
        [
            ("Людмила", "Русланова", "ул. Лермонтова, дом 12", "+79998888888"),
            ("Руслан", "Людмилов", "ул. Пушкина, д2", "+79998526936")
        ]
    )
    def test_order(self, locator, name, surname, address, phone):
        self.driver.get(BASE_URL)
        home_page = HomePage(self.driver)
        home_page.click_order_button(locator)
        assert self.driver.current_url == BASE_URL + "order"
        order_page = OrderPage(self.driver)
        order_page.fill_inputs(name, surname, address, phone)
        order_page.click_next_button()
        order_page.choose_date_of_delivery()
        order_page.choose_rent_time()
        order_page.choose_color()
        order_page.click_oder_button()
        assert order_page.is_overlay_visible() is True
        order_page.click_confirm_button()
        assert "оформлен" in order_page.get_modal_header_text()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
