from data import get_index_from_list
from locators.order_page_locators import *
from page_objects.page import Page


class OrderPage(Page):

    def fill_inputs(self, name, surname, address, phone):
        self.find_element_by_locator(NAME_INPUT_LOCATOR).send_keys(name)
        self.find_element_by_locator(SURNAME_INPUT_LOCATOR).send_keys(surname)
        self.find_element_by_locator(ADDRESS_INPUT_LOCATOR).send_keys(address)
        self.find_and_click_element(METRO_INPUT_LOCATOR)
        self.wait()
        metro_items = self.find_elements_by_locator(METRO_DROPDOWN)
        self.wait()
        metro_item = metro_items[get_index_from_list(metro_items)]
        self.scroll_to_element(metro_item)
        self.wait()
        self.click_element(metro_item)
        self.find_element_by_locator(PHONE_INPUT_LOCATOR).send_keys(phone)

    def click_next_button(self):
        self.find_and_click_element(NEXT_BUTTON_LOCATOR)

    def choose_date_of_delivery(self):
        self.find_and_click_element(DATE_PICKER_LOCATOR)
        dates = self.find_elements_by_locator(DATE_LOCATOR)
        # всегда выбираем последнюю доступную дату
        self.click_element(dates[len(dates) - 1])
        self.wait()

    def choose_rent_time(self):
        self.find_and_click_element(RENT_TIME_LOCATOR)
        rent_time_options = self.find_elements_by_locator(RENT_TIME_OPTION_LOCATOR)
        rent_time_option = rent_time_options[get_index_from_list(rent_time_options)]
        self.scroll_to_element(rent_time_option)
        rent_time_option.click()

    def choose_color(self):
        color_options = self.find_elements_by_locator(COLOR_LOCATOR)
        idx = get_index_from_list(color_options)
        element = color_options[idx]
        self.click_element(element)

    def click_oder_button(self):
        self.find_and_click_element(ORDER_BUTTON_LOCATOR)
        self.wait()

    def is_overlay_visible(self):
        return self.find_element_by_locator(ORDER_OVERLAY_LOCATOR) is not None

    def click_confirm_button(self):
        self.find_and_click_element(ORDER_CONFIRM_BUTTON_LOCATOR)

    def get_modal_header_text(self):
        return self.find_element_by_locator(ORDER_OVERLAY_HEADER_LOCATOR).text
