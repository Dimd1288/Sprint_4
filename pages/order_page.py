from selenium.webdriver.support import expected_conditions as ES

from locators.order_page_locators import OrderPageClientDataLocators, OrderPageDetailsLocators, \
    OrderConfirmModalLocators, OrderSuccessModalLocators
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class OrderPageClientDetails(BasePage):

    def check_page_header(self):
        self.check_element_is_displayed(*OrderPageClientDataLocators().page_header_locator)

    def set_client_name(self, name):
        self.set_input_value(*OrderPageClientDataLocators().client_name_locator, name)

    def set_client_surname(self, surname):
        self.set_input_value(*OrderPageClientDataLocators().client_surname_locator, surname)

    def set_client_address(self, address):
        self.set_input_value(*OrderPageClientDataLocators().client_address_locator, address)

    def select_subway_station(self, station):
        self.driver.find_element(*OrderPageClientDataLocators().client_subway_station_locator).send_keys(station)
        WebDriverWait(self.driver, 3) \
            .until(
            ES.visibility_of_element_located(OrderPageClientDataLocators().client_subway_station_list_element_locator))
        self.driver.find_element(*OrderPageClientDataLocators().client_subway_station_list_element_locator).click()

    def set_client_phone_number(self, number):
        self.set_input_value(*OrderPageClientDataLocators().client_phone_number_locator, number)

    def set_order_client_details(self, name, surname, address, station, number):
        self.set_client_name(name)
        self.set_client_surname(surname)
        self.set_client_address(address)
        self.select_subway_station(station)
        self.set_client_phone_number(number)

    def click_next_step_button(self):
        self.driver.find_element(*OrderPageClientDataLocators().next_step_button_locator).click()


class OrderPageOrderData(BasePage):

    def check_page_header(self):
        self.check_element_is_displayed(*OrderPageDetailsLocators.page_header_locator)

    def set_order_date(self, date):
        self.set_input_value(*OrderPageDetailsLocators.date_locator, date)
        self.driver.find_element(*OrderPageDetailsLocators.page_header_locator).click()

    def select_rent_duration(self, days_amount):
        self.driver.find_element(*OrderPageDetailsLocators().rent_duration_dropdown_root_locator).click()
        self.driver.find_elements(*OrderPageDetailsLocators().rent_duration_dropdown_element_locator)[days_amount - 1] \
            .click()

    def select_order_color(self, color):
        colors = self.driver.find_elements(*OrderPageDetailsLocators.order_color_label_locator)
        for item in colors:
            if item.text == color:
                item.click()

    def set_comment(self, comment):
        self.set_input_value(*OrderPageDetailsLocators.order_comment_locator, comment)

    def set_order_data(self, date, duration, color, comment):
        self.set_order_date(date)
        self.select_rent_duration(duration)
        self.select_order_color(color)
        self.set_comment(comment)

    def click_confirm_order_button(self):
        self.driver.find_element(*OrderPageDetailsLocators().next_step_button_locator).click()


class OrderPageConfirmModal(BasePage):

    def check_modal_is_displayed(self):
        self.check_element_is_displayed(*OrderConfirmModalLocators().modal_header_locator)

    def click_modal_submit_button(self):
        self.driver.find_element(*OrderConfirmModalLocators.modal_submit_button_locator).click()


class OrderPageSuccessModal(BasePage):

    def check_success_modal_is_displayed(self):
        self.check_element_is_displayed(*OrderSuccessModalLocators.modal_message_locator)

    def get_order_number(self):
        text = self.driver.find_element(*OrderSuccessModalLocators().modal_message_container_locator).text
        number = ""
        for char in text:
            if char.isdigit():
                number = number + char
        return number

    def click_order_status_button(self):
        self.driver.find_element(*OrderSuccessModalLocators().modal_check_status_button_locator).click()
