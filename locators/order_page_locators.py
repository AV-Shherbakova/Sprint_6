from selenium.webdriver.common.by import By

NAME_INPUT_LOCATOR = [By.XPATH, "//input[contains(@placeholder,'* Имя')]"]
SURNAME_INPUT_LOCATOR = [By.XPATH, "//input[contains(@placeholder,'* Фамилия')]"]
ADDRESS_INPUT_LOCATOR = [By.XPATH, "//input[contains(@placeholder,'* Адрес: куда привезти заказ')]"]
METRO_INPUT_LOCATOR = [By.XPATH, "//input[contains(@placeholder,'* Станция метро')]"]
PHONE_INPUT_LOCATOR = [By.XPATH, "//input[contains(@placeholder,'* Телефон: на него позвонит курьер')]"]
METRO_DROPDOWN = [By.CLASS_NAME, 'select-search__row']
NEXT_BUTTON_LOCATOR = [By.XPATH, ".//button[text()='Далее']"]
DATE_PICKER_LOCATOR = [By.CLASS_NAME, "react-datepicker__input-container"]
DATE_LOCATOR = [By.XPATH, "//div[contains(@class, 'react-datepicker__day')]"]
RENT_TIME_LOCATOR = [By.CLASS_NAME, "Dropdown-root"]
RENT_TIME_OPTION_LOCATOR = [By.CLASS_NAME, "Dropdown-option"]
COLOR_LOCATOR = [By.CLASS_NAME, "Checkbox_Label__3wxSf"]
ORDER_BUTTON_LOCATOR = [By.XPATH,
                        "//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Заказать']"]
ORDER_OVERLAY_LOCATOR = [By.CLASS_NAME, "Order_Overlay__3KW-T"]
ORDER_CONFIRM_BUTTON_LOCATOR = [By.XPATH,
                                "//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Да']"]
ORDER_OVERLAY_HEADER_LOCATOR = [By.CLASS_NAME, "Order_ModalHeader__3FDaJ"]
