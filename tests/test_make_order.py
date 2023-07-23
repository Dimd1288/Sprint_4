from selenium import webdriver
import pytest
from constants import MAIN_URL, USER_SET_1, USER_SET_2
from pages.order_page import OrderPageClientDetails, OrderPageOrderData, OrderPageSuccessModal, OrderPageConfirmModal
from pages.main_page import MainPage
from pages.order_status_page import OrderStatusPage
from pages.common_elements import CommonElements


class TestOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize("element,name,surname,address,station,phone,date,amount,color,comment",
                             [USER_SET_1, USER_SET_2])
    def test_create_order_is_successful(self, element, name, surname, address, station, phone, date, amount, color,
                                        comment):
        self.driver.get(MAIN_URL)
        client_data = OrderPageClientDetails(self.driver)
        order_data = OrderPageOrderData(self.driver)
        modal_confirm = OrderPageConfirmModal(self.driver)
        modal_success = OrderPageSuccessModal(self.driver)
        common = CommonElements(self.driver)
        common.click_order_button(element)
        client_data.check_page_header()
        client_data.set_order_client_details(name, surname, address, station, phone)
        client_data.click_next_step_button()
        order_data.check_page_header()
        order_data.set_order_data(date, amount, color, comment)
        order_data.click_confirm_order_button()
        modal_confirm.check_modal_is_displayed()
        modal_confirm.click_modal_submit_button()
        modal_success.check_success_modal_is_displayed()
        order = modal_success.get_order_number()
        modal_success.click_order_status_button()
        OrderStatusPage(self.driver).check_order_is_exist(order)
        common.click_home_link()
        MainPage(self.driver).check_home_header_is_displayed()
        common.check_yandex_link()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
