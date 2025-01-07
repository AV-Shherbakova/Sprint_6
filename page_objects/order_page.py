import time

from conftest import get_index_from_list, scroll_to_element
from locators.order_page_locators import *


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def fill_inputs(self, name, surname, address, phone):
        self.driver.find_element(*NAME_INPUT_LOCATOR).send_keys(name)
        self.driver.find_element(*SURNAME_INPUT_LOCATOR).send_keys(surname)
        self.driver.find_element(*ADDRESS_INPUT_LOCATOR).send_keys(address)
        self.driver.find_element(*METRO_INPUT_LOCATOR).click()
        time.sleep(0.05)
        metro_items = self.driver.find_elements(*METRO_DROPDOWN)
        time.sleep(0.5)
        metro_item = metro_items[get_index_from_list(metro_items)]
        scroll_to_element(self.driver, metro_item)
        time.sleep(0.05)
        metro_item.click()
        self.driver.find_element(*PHONE_INPUT_LOCATOR).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*NEXT_BUTTON_LOCATOR).click()

    def choose_date_of_delivery(self):
        self.driver.find_element(*DATE_PICKER_LOCATOR).click()
        dates = self.driver.find_elements(*DATE_LOCATOR)
        # всегда выбираем последнюю доступную дату
        dates[len(dates) - 1].click()
        time.sleep(0.5)

    def choose_rent_time(self):
        self.driver.find_element(*RENT_TIME_LOCATOR).click()
        rent_time_options = self.driver.find_elements(*RENT_TIME_OPTION_LOCATOR)
        rent_time_option = rent_time_options[get_index_from_list(rent_time_options)]
        scroll_to_element(self.driver, rent_time_option)
        rent_time_option.click()

    def choose_color(self):
        color_options = self.driver.find_elements(*COLOR_LOCATOR)
        color_options[get_index_from_list(color_options)].click()

    def click_oder_button(self):
        self.driver.find_element(*ORDER_BUTTON_LOCATOR).click()
        time.sleep(0.5)

    def is_overlay_visible(self):
        return self.driver.find_element(*ORDER_OVERLAY_LOCATOR) is not None

    def click_confirm_button(self):
        self.driver.find_element(*ORDER_CONFIRM_BUTTON_LOCATOR).click()

    def get_modal_header_text(self):
        header = self.driver.find_element(*ORDER_OVERLAY_HEADER_LOCATOR)
        return header.text
