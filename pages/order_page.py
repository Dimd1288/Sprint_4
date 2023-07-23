from selenium.webdriver.support import expected_conditions as ES

from locators.order_page_locators import OrderPageClientDataLocators, OrderPageDetailsLocators, \
    OrderConfirmModalLocators, OrderSuccessModalLocators
from selenium.webdriver.support.wait import WebDriverWait


class OrderPageClientDetails:

    def __init__(self, driver):
        self.driver = driver

    def check_page_header(self):
        assert self.driver.find_element(*OrderPageClientDataLocators().page_header_locator).is_displayed()

    def set_client_name(self, name):
        self.driver.find_element(*OrderPageClientDataLocators().client_name_locator).send_keys(name)

    def set_client_surname(self, surname):
        self.driver.find_element(*OrderPageClientDataLocators().client_surname_locator).send_keys(surname)

    def set_client_address(self, address):
        self.driver.find_element(*OrderPageClientDataLocators().client_address_locator).send_keys(address)

    def select_subway_station(self, station):
        self.driver.find_element(*OrderPageClientDataLocators().client_subway_station_locator).send_keys(station)
        WebDriverWait(self.driver, 3) \
            .until(
            ES.visibility_of_element_located(OrderPageClientDataLocators().client_subway_station_list_element_locator))
        self.driver.find_element(*OrderPageClientDataLocators().client_subway_station_list_element_locator).click()

    def set_client_phone_number(self, number):
        self.driver.find_element(*OrderPageClientDataLocators().client_phone_number_locator).send_keys(number)

    def set_order_client_details(self, name, surname, address, station, number):
        self.set_client_name(name)
        self.set_client_surname(surname)
        self.set_client_address(address)
        self.select_subway_station(station)
        self.set_client_phone_number(number)

    def click_next_step_button(self):
        self.driver.find_element(*OrderPageClientDataLocators().next_step_button_locator).click()


class OrderPageOrderData:
    def __init__(self, driver):
        self.driver = driver

    def check_page_header(self):
        assert self.driver.find_element(*OrderPageDetailsLocators.page_header_locator).is_displayed()

    def set_order_date(self, date):
        self.driver.find_element(*OrderPageDetailsLocators.date_locator).send_keys(date)
        self.driver.find_element(*OrderPageDetailsLocators.page_header_locator).click()

    def select_rent_duration(self, days_amount):
        self.driver.find_element(*OrderPageDetailsLocators().rent_duration_dropdown_root_locator).click()
        self.driver.find_elements(*OrderPageDetailsLocators().rent_duration_dropdown_element_locator)[days_amount - 1]\
            .click()

    def select_order_color(self, color):
        colors = self.driver.find_elements(*OrderPageDetailsLocators.order_color_label_locator)
        for item in colors:
            if item.text == color:
                item.click()

    def set_comment(self, comment):
        self.driver.find_element(*OrderPageDetailsLocators.order_comment_locator).send_keys(comment)

    def set_order_data(self, date, duration, color, comment):
        self.set_order_date(date)
        self.select_rent_duration(duration)
        self.select_order_color(color)
        self.set_comment(comment)

    def click_confirm_order_button(self):
        self.driver.find_element(*OrderPageDetailsLocators().next_step_button_locator).click()


class OrderPageConfirmModal:
    def __init__(self, driver):
        self.driver = driver

    def check_modal_is_displayed(self):
        assert self.driver.find_element(*OrderConfirmModalLocators().modal_header_locator).is_displayed()

    def click_modal_submit_button(self):
        self.driver.find_element(*OrderConfirmModalLocators.modal_submit_button_locator).click()


class OrderPageSuccessModal:

    def __init__(self, driver):
        self.driver = driver

    def check_success_modal_is_displayed(self):
        assert self.driver.find_element(*OrderSuccessModalLocators.modal_message_locator).is_displayed()

    def get_order_number(self):
        text = self.driver.find_element(*OrderSuccessModalLocators().modal_message_container_locator).text
        number = ""
        for char in text:
            if char.isdigit():
                number = number + char
        return number

    def click_order_status_button(self):
        self.driver.find_element(*OrderSuccessModalLocators().modal_check_status_button_locator).click()
